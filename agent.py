import os
import re
import json
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pyzotero import zotero
from firecrawl import FirecrawlApp
from crewai import Agent, Task, Crew, Process

# Load environment variables (for local runs)
load_dotenv()

# --- VALIDATE ENVIRONMENT ---
ZOTERO_USER_ID = os.getenv("ZOTERO_USER_ID")
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

if not all([ZOTERO_USER_ID, ZOTERO_API_KEY, FIRECRAWL_API_KEY]):
    print("Error: Missing required API keys in environment.")
    sys.exit(1)

# Initialize external integrations
zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY) # Private user library
firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# --- 1. THE SOURCE AGENT FUNCTIONS (Deduplication & Metadata) ---
def check_zotero_duplicate(url=None):
    """Checks Zotero API to ensure the source is not already indexed."""
    if not url:
        return False
    try:
        # Search library matching URL string
        results = zot.items(q=url)
        return len(results) > 0
    except Exception as e:
        print(f"Zotero duplication check failed: {e}")
        return False

def push_to_zotero(title, url, abstract, doi=None):
    """Generates a clean metadata item in Zotero."""
    try:
        # Request standard journal article template
        template = zot.item_template('journalArticle')
        template['title'] = title
        template['url'] = url
        template['abstractNote'] = abstract
        if doi:
            template['DOI'] = doi
        
        # Insert metadata via Write API
        zot.create_items([template])
        print(f"[Source] Successfully created Zotero metadata card for: {title}")
    except Exception as e:
        print(f"Failed to create Zotero record: {e}")

# --- 2. ARTIFACT ENGINE SKILLS (Deep Crawling) ---
def scrape_clean_markdown(url):
    """Scrapes any URL, Youtube video, or PDF word-for-word into structural Markdown."""
    try:
        # Firecrawl handles JavaScript, extracts transcripts, and strips out cookies/ads
        result = firecrawl.scrape_url(url, params={'formats': ['markdown']})
        return result.get('markdown', '')
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

# --- 3. RELEVANCE AGENT ---
relevance_agent = Agent(
    role="Relevance Gatekeeper",
    goal="Distinguish high-academic rigor (scholarly papers/syllabi) from informal commentary.",
    backstory=(
        "You are an academic reviewer. You evaluate incoming UX x HAII educational text. "
        "Your job is to decide whether content is rigorous (PUBLISH) or informal/speculative (HOLD)."
    ),
    verbose=True
)

# --- 4. ENGINE PIPELINE CONTROLLER ---
def run_pipeline(url_list):
    """Processes URLs through the Six-Agent constraints."""
    for url in url_list:
        print(f"\n[Orchestrator] Target found: {url}")
        
        # Source Deduplication Step
        if check_zotero_duplicate(url=url):
            print(f"[Source] Source already exists in Zotero. Skipping pipeline.")
            continue
            
        # Artifact Extraction Step (Word-for-Word Transcription)
        markdown_content = scrape_clean_markdown(url)
        if not markdown_content or len(markdown_content) < 200:
            print(f"[Artifact] Content extraction failed or text is too short. Skipping.")
            continue

        # Relevance Verification Step (Grading Engine)
        eval_task = Task(
            description=(
                f"Evaluate the following extracted text block: \n\n{markdown_content[:6000]}\n\n"
                "Determine the classification:\n"
                "1. Choose 'PUBLISH' if it is a peer-reviewed paper, conference proceeding, university syllabus, or technical documentation (e.g. Google/Microsoft research).\n"
                "2. Choose 'HOLD' if it is a Medium article, casual design blog post, podcast, or speculative YouTube commentary.\n\n"
                "Provide your response strictly in the following JSON format:\n"
                "{\n"
                "  \"decision\": \"PUBLISH\" or \"HOLD\",\n"
                "  \"rationale\": \"Why it was categorized this way\",\n"
                "  \"title\": \"The clean title of the resource\",\n"
                "  \"doi\": \"DOI number if available, otherwise empty\"\n"
                "}"
            ),
            expected_output="A JSON string evaluating the resource.",
            agent=relevance_agent
        )
        
        crew = Crew(agents=[relevance_agent], tasks=[eval_task], process=Process.sequential)
        judgment_str = str(crew.kickoff())
        
        # Safely parse agent's JSON response
        try:
            json_match = re.search(r'\{.*\}', judgment_str, re.DOTALL)
            judgment = json.loads(json_match.group(0))
        except Exception:
            judgment = {"decision": "HOLD", "title": "Manual Verification Required", "doi": "", "rationale": "Parsing failed."}

        decision = judgment.get('decision', 'HOLD')
        title = judgment.get('title', 'Unknown Title')
        doi = judgment.get('doi', '')
        rationale = judgment.get('rationale', '')

        # Push clean metadata down to Zotero (Source layer)
        push_to_zotero(title, url, rationale, doi)

        # Write clean Frontmatter and markdown transcript to Git (Publication layer)
        frontmatter = (
            "---\n"
            f"title: \"{title}\"\n"
            f"source_url: \"{url}\"\n"
            f"doi: \"{doi}\"\n"
            f"ingest_date: \"{datetime.now().strftime('%Y-%m-%d')}\"\n"
            f"status: \"{decision.lower()}\"\n"
            "---\n\n"
        )
        final_doc = frontmatter + markdown_content
        
        # Save to correct folder destination
        subfolder = "vault" if decision == "PUBLISH" else "hold_review"
        safe_filename = re.sub(r'[^a-zA-Z0-9]', '_', title)[:60].lower() + ".md"
        file_path = f"docs/{subfolder}/{safe_filename}"
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_doc)
            
        print(f"[Publication] Word-for-word file written locally: {file_path}")

if __name__ == "__main__":
    # Test Sweep
    target_links = [
        "https://arxiv.org/html/2403.04615v1",
        "https://medium.com/design-bootcamp/designing-ai-ux-principles-a5cb70df4a78"
    ]
    run_pipeline(target_links)
