import os
import re
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pyzotero import zotero
from firecrawl import FirecrawlApp
from crewai import Agent, Task, Crew, Process
from langchain_community.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Validate Keys
ZOTERO_USER_ID = os.getenv("ZOTERO_USER_ID")
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

if not all([ZOTERO_USER_ID, ZOTERO_API_KEY, FIRECRAWL_API_KEY]):
    print("Error: Missing required API keys in environment.")
    sys.exit(1)

# Initialize integrations
zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY)
firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# --- 1. DYNAMIC DISCOVERY SKILLS (THE SCOUT) ---

def discover_web_links(query, limit=10):
    """Uses Firecrawl's Search API to find live web pages, PDFs, and YouTube videos."""
    print(f"[Scout] Searching the web for: '{query}'...")
    try:
        # Firecrawl search fetches the top matching URLs across the live internet
        search_results = firecrawl.search(query, params={'limit': limit})
        urls = [item.get('url') for item in search_results if item.get('url')]
        print(f"[Scout] Web Search found {len(urls)} candidates.")
        return urls
    except Exception as e:
        print(f"Web search failed: {e}")
        return []

def discover_academic_papers(query, limit=10):
    """Queries the completely free arXiv API for peer-reviewed papers on the topic."""
    print(f"[Scout] Searching arXiv academic database for: '{query}'...")
    try:
        # Formulate API search URL
        formatted_query = query.replace(" ", "+AND+")
        api_url = f"http://export.arxiv.org/api/query?search_query=all:{formatted_query}&max_results={limit}"
        
        # Pull data
        response = urllib.request.urlopen(api_url)
        xml_data = response.read()
        
        # Parse XML to pull links
        root = ET.fromstring(xml_data)
        urls = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            id_url = entry.find('{http://www.w3.org/2005/Atom}id').text
            # Convert abstract viewer URL to direct PDF paper URL
            pdf_url = id_url.replace("abs", "pdf")
            urls.append(pdf_url)
            
        print(f"[Scout] arXiv database found {len(urls)} academic candidates.")
        return urls
    except Exception as e:
        print(f"Academic search failed: {e}")
        return []

# --- 2. SOURCE AGENT SKILLS (Deduplication) ---

def check_zotero_duplicate(url=None):
    """Checks Zotero API to ensure we don't process a duplicate link."""
    if not url:
        return False
    try:
        results = zot.items(q=url)
        return len(results) > 0
    except Exception as e:
        print(f"Zotero duplication check failed: {e}")
        return False

def push_to_zotero(title, url, abstract, doi=None):
    """Pushes a clean metadata item to Zotero."""
    try:
        template = zot.item_template('journalArticle')
        template['title'] = title
        template['url'] = url
        template['abstractNote'] = abstract
        if doi:
            template['DOI'] = doi
        zot.create_items([template])
        print(f"[Source] Successfully registered citation in Zotero.")
    except Exception as e:
        print(f"Failed to create Zotero record: {e}")

# --- 3. ARTIFACT SKILLS (Extraction) ---

def scrape_clean_markdown(url):
    """Scrapes any URL, PDF, or document word-for-word into Markdown."""
    try:
        result = firecrawl.scrape_url(url, params={'formats': ['markdown']})
        return result.get('markdown', '')
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

# --- 4. RELEVANCE AGENT ---

relevance_agent = Agent(
    role="Relevance Gatekeeper",
    goal="Distinguish high-academic rigor (scholarly papers/syllabi) from informal commentary.",
    backstory=(
        "You are an academic reviewer. You evaluate incoming UX x HAII educational text. "
        "Your job is to decide whether content is rigorous (PUBLISH) or informal/speculative (HOLD)."
    ),
    llm=ChatOpenAI(model_name="gpt-4o-mini"),
    verbose=True
)

# --- 5. RUN ENGINE ---

def run_pipeline(url_list):
    """Processes discovered URLs through our Six-Agent constraints."""
    for url in url_list:
        print(f"\n[Orchestrator] Processing: {url}")
        
        # Deduplication Check
        if check_zotero_duplicate(url=url):
            print(f"[Source] Link already exists in Zotero. Skipping.")
            continue
            
        # Extract Full Document Word-for-Word
        markdown_content = scrape_clean_markdown(url)
        if not markdown_content or len(markdown_content) < 200:
            print(f"[Artifact] No substantative text extracted. Skipping.")
            continue

        # Evaluate Relevance
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
        
        # Safe JSON parse
        try:
            json_match = re.search(r'\{.*\}', judgment_str, re.DOTALL)
            judgment = json.loads(json_match.group(0))
        except Exception:
            judgment = {"decision": "HOLD", "title": "Manual Verification Required", "doi": "", "rationale": "Parsing failed."}

        decision = judgment.get('decision', 'HOLD')
        title = judgment.get('title', 'Unknown Title')
        doi = judgment.get('doi', '')
        rationale = judgment.get('rationale', '')

        # Record metadata to Zotero (Source)
        push_to_zotero(title, url, rationale, doi)

        # Write clean Frontmatter and markdown transcript to Git (Publication)
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
        
        # Path logic mapping Context
        subfolder = "vault" if decision == "PUBLISH" else "hold_review"
        safe_filename = re.sub(r'[^a-zA-Z0-9]', '_', title)[:60].lower() + ".md"
        file_path = f"docs/{subfolder}/{safe_filename}"
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_doc)
            
        print(f"[Publication] Word-for-word file written locally: {file_path}")

if __name__ == "__main__":
    # --- SEARCH MASTER KEYWORDS ---
    search_queries = [
        "human ai interaction UX design",
        "HAII design guidelines",
        "explainable AI design patterns"
    ]
    
    discovered_pool = []
    
    # Run the Scout to pull links
    for query in search_queries:
        # Collect 5 web links & 5 academic papers per term
        discovered_pool.extend(discover_web_links(query, limit=5))
        discovered_pool.extend(discover_academic_papers(query, limit=5))
    
    # Remove duplicates within this specific run pool
    unique_pool = list(set(discovered_pool))
    print(f"\n[Orchestrator] Target discovery complete! Found {len(unique_pool)} unique sources.")
    
    # Start the assembly line!
    run_pipeline(unique_pool)
