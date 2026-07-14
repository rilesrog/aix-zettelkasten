---
title: "Explainable AI for Blind and Low-Vision Users: Navigating Trust, Modality, and Interpretability in the Agentic Era"
source_url: "http://arxiv.org/pdf/2604.00187v2"
doi: "10.1145/nnnnnnn.nnnnnnn"
ingest_date: "2026-07-14"
status: "publish"
---

arXiv:2604.00187v2 \[cs.HC\] 2 May 2026

## [https://arxiv.org/abs/2604.00187v2](https://arxiv.org/abs/2604.00187v2)

# Explainable AI for Blind and Low-Vision Users: Navigating Trust, Modality, and Interpretability in the Agentic Era

## [https://orcid.org/0000-0002-0761-035X](https://orcid.org/0000-0002-0761-035X) Abu Noman Md Sakib

## [https://orcid.org/0009-0006-4089-5111](https://orcid.org/0009-0006-4089-5111) Protik Dey

Abu Noman Md Sakib
[abunomanmd.sakib@utsa.edu](mailto:abunomanmd.sakib@utsa.edu)
University of Texas at San Antonio
San Antonio, Texas, USA

Zijie Zhang
[zijie.zhang@utsa.edu](mailto:zijie.zhang@utsa.edu)
University of Texas at San Antonio
San Antonio, Texas, USA

## Abstract

Explainable Artificial Intelligence (XAI) is critical for ensuring trust
and accountability, yet its development remains predominantly visual. For blind and low-vision (BLV) users, the lack of accessible
explanations creates a fundamental barrier to the independent use
of AI-driven assistive technologies. This problem intensifies as AI
systems shift from single-query tools into autonomous agents that
take multi-step actions and make consequential decisions across extended task horizons, where a single undetected error can propagate
irreversibly before any feedback is available. This paper investigates
the unique XAI requirements of the BLV community through a comprehensive analysis of user interviews and contemporary research.
By examining usage patterns across environmental perception and
decision support, we identify a significant modality gap. Empirical
evidence suggests that while BLV users highly value conversational
explanations, they frequently experience “self-blame” for AI failures.
The paper concludes with a research agenda for accessible Explainable AI in agentic systems, advocating for multimodal interfaces,
blame-aware explanation design, and participatory development.

•Human-centered computing → Accessibility systems and
tools; _Empirical studies in accessibility_; _Empirical studies in HCI_;•
Computing methodologies → _Philosophical/theoretical founda-_ _tions of artificial intelligence_.

Protik Dey
[protik.dey@utsa.edu](mailto:protik.dey@utsa.edu)
University of Texas at San Antonio
San Antonio, Texas, USA

## [https://orcid.org/0000-0003-1254-098X](https://orcid.org/0000-0003-1254-098X) Zijie Zhang

## [https://orcid.org/0000-0002-0686-1448](https://orcid.org/0000-0002-0686-1448) Taslima Akter

## 1 Introduction

## Keywords Explainable AI, Blind and Low-Vision, HCXAI, Accessibility, Agen-

Explainable AI, Blind and Low-Vision, HCXAI, Accessibility, Agentic AI
arXiv:2604.00187v2 \[cs.HC\] 2 May 2026

Taslima Akter
[taslima.akter@utsa.edu](mailto:taslima.akter@utsa.edu)
University of Texas at San Antonio
San Antonio, Texas, USA

_Human-centered Explainable AI Workshop (HCXAI) @ CHI 2026, Barcelona, Spain_
2026\. ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM
[https://doi.org/10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

With the introduction of vision models and large language models
(LLMs), AI systems can now describe scenes, recognize objects,
and interpret complex environments in real time. For many BLV
individuals, these tools are no longer just convenient. They have
become essential aids that change how people navigate the physical world \[20\]. However, these systems are rapidly evolving from
simple description tools into autonomous agents that plan multistep task sequences, invoke external tools, and take actions with
real-world consequences. Because their inner workings remain a
“black box,” this shift creates an especially acute challenge for the
BLV community \[16\]. A sighted user who sees an agent draft a
message or confirm a purchase can interrupt if something looks
wrong. A BLV user has no equivalent monitoring channel. An error in Step 2 of a 10-step task can propagate silently through all
subsequent steps and result in an irreversible outcome before any
feedback is received. An AI system’s output is often the primary
source of environmental truth for a BLV user. Sometimes, it is the
only source. Without accessible ways to inspect how the agent
made its decisions, users cannot detect hallucinations, erroneous
tool invocations, or cascading misinterpretations \[2\]. The current
approach to Explainable AI (XAI) makes this problem worse. The
Human-Centered Explainable AI (HCXAI) movement tries to look
beyond math and understand how people actually use explanations
\[10\]. Yet, mainstream XAI methods like SHAP \[14\] and GradCAM
\[19\] still rely heavily on visuals. By using color-coded heatmaps
and visual bounding boxes, traditional XAI shuts out the exact users
who rely on AI the most for sensory translation.
This paper addresses that gap by exploring accessible XAI and
arXiv:2604.00187v2 \[cs.HC\] 2 May 2026

This paper addresses that gap by exploring accessible XAI and
user trust within the BLV community. We look at how trust changes
arXiv:2604.00187v2 \[cs.HC\] 2 May 2026depending on the stakes of the situation. We also highlight a common “Self-Blame Bias.” This occurs when BLV users blame themselves for taking a bad photo rather than realizing the AI made
a mistake. We then evaluate which types of explanations work
best for verifying information and supporting decisions, comparing
formats like system rules against conversational interactions. We
argue that real digital inclusion for the BLV community requires
legitimacy across the entire AI pipeline. This means everything
from using representative training data to building clear, non-visual
ways for users to understand AI decisions.

* * *

## 2 Related Work

2 Related Work
Recent work in HCXAI highlights that explanations must be tailored to the people actually using them \[10, 11, 18\]. However, most
mainstream methods for computer vision still rely on visual cues
like heatmaps, which completely exclude BLV users \[13\]. To fix this,
accessible XAI focuses on translating model logic into non-visual
formats like text or conversation. This is especially important because BLV users face unique challenges with trust. As AI moves
from simple object recognition to complex, multi-step autonomous
agents, this overreliance creates serious epistemological vulnerability \[5, 8\]. If a system confidently hallucinates early in a task,
the user has no easy way to catch the error \[9\]. Researchers have
suggested using conversational AI to introduce “cognitive forcing,”
encouraging users to ask questions and double-check outputs rather
than passively accepting them \[6, 7\]. Some studies indicate that
BLV users develop complex, often flawed, mental models of Generative AI, sometimes viewing these tools as authoritative rather than
probabilistic systems prone to hallucination \[1\]. Furthermore, trust
in these systems is highly contextual. Xinru et al. demonstrated in
their framework that users’ acceptance of technical failures is not
binary but contingent on the stakes of the task and the social environment \[22\]. Accessible XAI must support explorable interactions
that allow users to interrogate these stakes \[21\]. We view all of these
challenges which argues that an AI system is only valid if it centers
the people impacted by its decisions. For the BLV community, this
means building legitimacy directly into the pipeline, starting with
training data that actually reflects how they take photos, all the
way to providing transparent, non-visual ways to verify what the
AI is doing.
The emergence of LLM-based agents introduces explainability de-

AI is doing.
The emergence of LLM-based agents introduces explainability demands that go beyond explaining a single model prediction. Agentic
systems orchestrate chains of reasoning steps, invoke external tools,
and produce execution traces that unfold over time \[9\]. The relevant unit of explanation is no longer a feature attribution score but
a process trace: which sub-goals were set, which tools were called,
and where the agent chose to act rather than verify. The proxy verification strategies BLV users rely on today (barcode cross-checking,
multi-shot photography, human fallback) are workarounds for the
absence of accessible process transparency. These workarounds
do not scale to agentic pipelines. A user cannot take three photos
of an agent’s multi-step scheduling decision. This makes the BLV
community a critical test case for agentic XAI design.

We conducted semi-structured interviews with six BLV participants
so far with prior experience using GenAI tools, including generalpurpose systems such as ChatGPT, Google Gemini, Meta AI, and
Microsoft Copilot, as well as GenAI-powered assistive technologies
such as Be My AI, Seeing AI, and Aira. Recruitment was conducted
through the National Federation of the Blind, with a small number
of participants recruited via snowball sampling. Interested individuals completed an online recruitment form, which also served as
a screening form to assess eligibility. Eligibility criteria included:
(1) residing in the United States, (2) age 18 years or older, (3) identify
as blind or low vision, (4) primarily use a screen reader for accessing
digital content (instead of magnification), (5) speak English, and

## 3 Methodology

(6) have experience of using GenAI tools. One researcher contacted
each eligible participant via email to schedule the interviews.
Most of the participants are moderate users of GenAI tools, with

Most of the participants are moderate users of GenAI tools, with
two participants reported using them frequently, and one participant mentioned having comparatively less experience. All participants use GenAI-powered assistive technologies such as Be My AI,
Seeing AI, Aira, etc. To access these GenAI tools, all participants
reported using screen readers like JAWS, NVDA, and VoiceOver.
Out of the six participants, five were females (83.33%) and one participant was male (16.67%). One participant was in the 18-29 age
group, three were in the 40-49 range, one reported being between
50 to 59 years old, and one participant was aged 60 or above.
The interviews were conducted remotely via Zoom, following

The interviews were conducted remotely via Zoom, following
approval from our university’s Institutional Review Board (IRB).
Participants were provided with an informed consent form and a
demographic form when the schedule was fixed via email. At the
beginning of each interview session, the interviewer introduced the
study goals, interview process, and obtained participants’ verbal
consent to proceed.
The interview protocol was designed to investigate the partic-

consent to proceed.
The interview protocol was designed to investigate the participants’ experiences of using the GenAI tools and what kind of
explanation formats contribute to more trustworthy GenAI tools.
In the first part of the interview, we asked the participants to share
their current interaction with the GenAI tools. The second part
of the interview explored participants’ perceptions of trust and
understanding of AI systems through two scenario-based discussions, examining how different explanation styles (e.g., descriptive
details, rules, comparisons, and interactive dialogue) influenced
accessibility, trust, and decision-making. These two scenarios include object identification and decision support. In the final part,
participants were invited to share recommendations for developers
and researchers on designing accessible explanation mechanisms
that help BLV users better understand and trust AI response.
The interviews typically lasted between 45 and 60 minutes. All

that help BLV users better understand and trust AI response.
The interviews typically lasted between 45 and 60 minutes. All
interviews were video-recorded with participants’ permission and
later transcribed for analysis. Participants received a US$30 Amazon
gift card as compensation for their participation.
For data analysis, two authors independently participated in the

For data analysis, two authors independently participated in the
coding process using a reflexive thematic analysis approach \[4\].
Inter-rater reliability was not calculated, as such metrics are not
considered suitable for interview-based data where codes are not
fixed \[15, 17\]. Instead, the authors met weekly to discuss codes,
resolve differences to ensure consistency, and come up with themes.

Our analysis reveals that trust in AI for BLV users is not a static
property of the system but a dynamic negotiation between the
user’s perception of risk and the system’s mode of communication.
We structure these findings across three dimensions: the calibration
of trust relative to risk, the preference for conversational modalities
to resolve ambiguity, and the strategies users employ to verify
non-interpretable outputs.

## 4 Findings Our analysis reveals that trust in AI for BLV users is not a static

* * *

## 4.1 The Paradox of Trust: Risk Calibration and the Self-Blame Bias

Participants demonstrated a sophisticated ability to calibrate trust
based on the “stakes” of a given task. Trust was not binary; rather,
it functioned as a sliding scale dependent on the consequence of
error. P1 explicitly distinguished between low-stakes convenience
and high-stakes health decisions:

“If it’s medicine, I am not going to trust the AI 100%. I
will double-check. But if it is just a can of soda, I don’t

will double-check. But if it is just a can of soda, I don’t
care if it is Coke or Pepsi.” (P1)

care if it is Coke or Pepsi.” (P1)

This distinction shows that users do not view AI reliability as a
single fixed quality. Instead, they are willing to accept mistakes for
convenient tasks while demanding strict accuracy for safety-critical
situations. However, this calibration is frequently undermined by
a pervasive “Self-Blame Bias.” When low-stakes errors occurred,
participants often attributed the failure to their own actions, such as
camera alignment or lighting, rather than questioning the model’s
capabilities. P3 described this internalization of failure as a primary
barrier to effectively critiquing the system:
“It’s garbage in, garbage out. If I don’t give it a good

“It’s garbage in, garbage out. If I don’t give it a good
picture... if I don’t have the lighting right, or if I’m too
close or too far away, it can’t tell me what it is.” (P3)
The absence of specific feedback leads users to interpret model

The absence of specific feedback leads users to interpret model
failure as a personal failure of execution. They assume the algorithm
is functioning correctly, but it is simply limited by the quality of the
input they provided. This tendency to assume “user error” protects
the model from scrutiny. Unlike sighted users who can instantly
verify if a model has hallucinated, BLV users often lack the ground
truth to distinguish between a bad photo and a bad prediction. P2
highlighted how hallucinations shatter this trust entirely, as the
user cannot easily verify which part of the description is real:
“Sometimes it hallucinates... it will make up things

“Sometimes it hallucinates... it will make up things
that aren’t there just to give me an answer. That makes
me really hesitant.” (P2)

## 4.2 Beyond Description: Conversational Agents as Tools for Contestability A recurring frustration among participants was the “Whole Scene

A recurring frustration among participants was the “Whole Scene
Bias,” where vision-to-language models prioritize generic scene
descriptions over the user’s specific intent. P4 expressed that standard captioning often obscures critical information with irrelevant
background details:
“It’s describing the whole scene, not a specific item.

“It’s describing the whole scene, not a specific item.
And what if you just want a specific item? ... I don’t

need to know there’s a table there.” (P4)

These overly detailed descriptions create a significant problem
with noise. By treating every visual detail as equally important,

and the AI is acting weird, I just hang up and call \[a gate this, participants overwhelmingly preferred conversational,\
conversation served as a mechanism for functional contestability.\
It allowed users to refine the system’s focus and correct initial mis-\
\
the interaction from a passive reception of information to an active\
negotiation:\
\
“I like the back and forth... almost like a conversation.\
‘Are you sure that’s a red shirt?’ and it says, ‘Oh, sorry,\
looking closer, it is actually maroon.”’ (P3)\
\
This interaction shifts the control from the system back to the\
user. Rather than passively accepting a static text, the user can\
actively question the AI’s confidence and guide its attention toward\
the specific object they are looking for. Furthermore, P2 argued for\
a “progressive disclosure” architecture, where the system provides\
a high-level summary first, allowing the user to query for details\
only if necessary. _“I would like a short description first... and then_ _maybe a button or an option to say ‘tell me more’... I don’t want a_\
\*paragraph every time.”\*shared P2. This approach reduces cognitive\
load during real-time navigation.\
\
## 4.3 Verification in the Dark: Proxy Strategies and the Human Fallback\
\
Lacking direct visual access to verify AI outputs, participants developed complex “proxy” strategies to triangulate the truth. These\
strategies often relied on redundancy or determinist data sources\
(like barcodes) to audit the probabilistic outputs of computer vision.\
P5 described a multi-modal verification process:\
\
“I scan the barcode first. If the barcode says ‘Beans’,\
then I see if the AI describes the can as beans. That’s\
how I check.” (P5)\
\
In this workflow, the barcode acts as a trusted fact that anchors\
the description. The user leverages this hard data to validate the\
often uncertain output of the computer vision model and builds\
trust through consistency rather than blind faith. Similarly, P1\
utilized a “multi-shot” strategy, manually creating an ensemble of\
predictions to reach a confidence threshold that the system failed\
to provide:\
“I usually take 3 or 4 pictures from different angles\
\
“I usually take 3 or 4 pictures from different angles\
just to be sure. If it says ‘bottle’ three times, then I\
believe it.” (P1)\
\
The user is effectively performing the manual work of error\
correction that the system should handle automatically. While this\
strategy reduces the risk of a single bad prediction, it takes a significant amount of time and effort to perform for every object. However,\
these workarounds have an upper limit. When the AI’s output remained ambiguous or inconsistent in high-stakes scenarios (e.g.,\
reading currency or documents), participants hit a hard limit on\
interpretability. In these instances, P2 noted that the only viable\
solution was to abandon the automated system entirely for human\
assistance:\
“If I really need to know, like for a document or money,\
\
This reliance on human fallback indicates that current explainability methods fail to provide sufficient standalone evidence for\
users to resolve uncertainty without external aid.\
\
* * *\
\
## 5 Discussion\
\
471 (Nov. 2022), 23 pages. doi:10.1145/3555572 [https://doi.org/10.1145/3555572](https://doi.org/10.1145/3555572)\
\
The central challenge for XAI in the non-visual context shifts from\
understanding model architecture to verifying immediate outcomes\
without visual ground truth. Our analysis reveals that the prevailing self-blame bias where users attribute system failures to\
their own photography rather than model uncertainty obscures the\
need for algorithmic accountability. To mitigate this, XAI design\
must transition from static descriptions to blame-aware interfaces\
that explicitly signal input quality issues and support functional\
contestability through conversational modalities. Our participants\
clearly preferred a “back-and-forth” interaction where they could\
ask to challenge the AI’s confidence and force it to double-check\
its work. By allowing users to challenge the system’s logic and\
demanding non-visual evidence rather than accepting a black-box\
output, future systems can bridge the verification gap that currently\
forces users to abandon automated tools for human assistance in\
high-stakes scenarios. This gap becomes more consequential in\
agentic settings. A user who misattributes an agent’s error to their\
own input in one step of a multi-step task will continue participating in a pipeline that is already off course. The human fallback\
strategy our participants rely on is also no longer viable when the\
agent has already sent a message, submitted a form, or confirmed a\
transaction. Future agentic systems must support step-level attribution, distinguishing input quality failures from model errors at\
each stage, and must seek explicit user confirmation before taking\
irreversible actions. The conversational, back-and-forth modality\
our participants preferred maps directly onto this need: an agent\
that can say “I selected this result because it matched your prior\
preference” and accept a follow-up challenge is far safer for BLV\
users than one that acts silently.\
\
This paper highlights how BLV users experience and evaluate the\
explainability in AI systems. Our findings demonstrate that trust\
is shaped by task risk and that users often internalize AI failures\
as their own mistakes. Participants consistently valued conversational explanations that allowed them to ask follow-up questions\
and resolve uncertainty. These results point to the limits of visually\
grounded XAI and emphasize the need for non visual, interactive explanation design. As AI systems take on more agentic roles, the cost\
of explanatory inaccessibility rises sharply. Multi-step pipelines,\
tool invocations, and irreversible actions make the self-blame bias\
more dangerous, the conversational verification strategies our participants valued more necessary, and the human fallback less available. Accessible agentic explainability is not a niche problem. It\
is a test of whether human-centered XAI can deliver on its core\
commitments.\
\
\[1\] Rudaiba Adnin and Maitraye Das. 2024. "I look at it as the king of knowledge":\
How Blind People Use and Understand Generative AI Tools. In _Proceedings of the_ _26th International ACM SIGACCESS Conference on Computers and Accessibility_(St.\
John’s, NL, Canada) _(ASSETS ’24)_. Association for Computing Machinery, New\
York, NY, USA, Article 64, 14 pages. doi:10.1145/3663548.3675631\
\[2\] Rahaf Alharbi, Angela D Cheong, Jaylin Herskovitz, Robin N. Brewer, and Sarita\
Schoenebeck. 2025. “Trying to Piece It Together”: Exploring Accessible Error\
Detection in Emerging Privacy Techniques With Blind People. In _Proceedings of_ _the 27th International ACM SIGACCESS Conference on Computers and Accessibility_\
\
_(ASSETS ’25)_. Association for Computing Machinery, New York, NY, USA, Article\
18, 20 pages. doi:10.1145/3663547.3746376\
\[3\] Rahaf Alharbi, Pa Lor, Jaylin Herskovitz, Sarita Schoenebeck, and Robin N. Brewer.\
2024\. Misfitting With AI: How Blind People Verify and Contest AI Errors. In\
_Proceedings of the 26th International ACM SIGACCESS Conference on Computers_ _and Accessibility_(St. John’s, NL, Canada) _(ASSETS ’24)_. Association for Computing\
Machinery, New York, NY, USA, Article 61, 17 pages. doi:10.1145/3663548.3675659\
\[4\] Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology.\
_Qualitative research in psychology_ 3, 2 (2006), 77–101.\
\[5\] Shiye Cao and Chien-Ming Huang. 2022. Understanding User Reliance on AI in\
Assisted Decision-Making. _Proc. ACM Hum.-Comput. Interact.6, CSCW2, Article_\
_471 (Nov. 2022), 23 pages. doi:10.1145/3555572_\
_\[6\] Yu-An Chen, Zicheng Zhu, and Yi-Chieh Lee. 2025. Humans Help Conversational_\
_AI: Exploring the Impact of Perceived AI Deservingness on People’s Decisions to_\
_Help and Their Perceptions on AI Seeking Help. InProceedings of the Extended_ _Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI_ _EA ’25)_. Association for Computing Machinery, New York, NY, USA, Article 329,\
8 pages. doi:10.1145/3706599.3720012\
\[7\] Elijah L. Claggett, Robert E. Kraut, and Hirokazu Shirado. 2025. Relational AI:\
Facilitating Intergroup Cooperation with Socially Aware Conversational Support.\
In _Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems_ _(CHI ’25)_. Association for Computing Machinery, New York, NY, USA, Article\
170, 22 pages. doi:10.1145/3706598.3713757\
\[8\] Sven Eckhardt, Niklas Kühl, Mateusz Dolata, and Gerhard Schwabe. 2025. A\
Survey of AI Reliance. _ACM Comput. Surv.58, 6, Article 161 (Dec. 2025), 37 pages._\
_doi:10.1145/3776528_\
_\[9\] Upol Ehsan, Elizabeth A Watkins, Philipp Wintersberger, Carina Manger, Nina_\
_Hubig, Saiph Savage, Justin D. Weisz, and Andreas Riener. 2025. New Frontiers of_\
_Human-centered Explainable AI (HCXAI): Participatory Civic AI, Benchmarking_\
_LLMs, XAI Hallucinations, and Responsible AI Audits. InProceedings of the_ _Extended Abstracts of the CHI Conference on Human Factors in Computing Systems_ _(CHI EA ’25)_. Association for Computing Machinery, New York, NY, USA, Article\
793, 6 pages. doi:10.1145/3706599.3706713\
\[10\] Upol Ehsan, Philipp Wintersberger, Q. Vera Liao, Elizabeth Anne Watkins, Carina\
Manger, Hal Daumé III, Andreas Riener, and Mark O Riedl. 2022. Human-Centered\
Explainable AI (HCXAI): Beyond Opening the Black-Box of AI. In _Extended_ _Abstracts of the 2022 CHI Conference on Human Factors in Computing Systems_\
(New Orleans, LA, USA) _(CHI EA ’22)_. Association for Computing Machinery,\
New York, NY, USA, Article 109, 7 pages. doi:10.1145/3491101.3503727\
\[11\] Upol Ehsan, Philipp Wintersberger, Elizabeth A Watkins, Carina Manger, Gonzalo\
Ramos, Justin D Weisz, Hal Daumé Iii, Andreas Riener, and Mark O Riedl. 2023.\
Human-centered explainable AI (HCXAI): coming of age. In _Extended abstracts_ _of the 2023 CHI conference on human factors in computing systems_. 1–7.\
\[12\] Jonggi Hong. 2018. Accessible Human-Error Interactions in AI Applications for\
the Blind. In _Proceedings of the 2018 ACM International Joint Conference and 2018_ _International Symposium on Pervasive and Ubiquitous Computing and Wearable_ _Computers_(Singapore, Singapore) _(UbiComp ’18)_. Association for Computing\
Machinery, New York, NY, USA, 522–528. doi:10.1145/3267305.3267321\
\[13\] Gyeongri Kim, Jiho Kim, and Yea-Seul Kim. 2023. “Explain What a Treemap\
is”: Exploratory Investigation of Strategies for Explaining Unfamiliar Chart to\
Blind and Low Vision Users. In _Proceedings of the 2023 CHI Conference on Human_ _Factors in Computing Systems_(Hamburg, Germany) _(CHI ’23)_. Association for\
Computing Machinery, New York, NY, USA, Article 805, 13 pages. doi:10.1145/\
3544548.3581139\
\[14\] Scott M Lundberg and Su-In Lee. 2017. A unified approach to interpreting model\
predictions. _Advances in neural information processing systems_ 30 (2017).\
\[15\] Nora McDonald, Sarita Schoenebeck, and Andrea Forte. 2019. Reliability and\
inter-rater reliability in qualitative research: Norms and guidelines for CSCW and\
HCI practice. _Proceedings of the ACM on human-computer interaction_ 3, CSCW\
(2019), 1–23.\
\[16\] Cecily Morrison, Martin Grayson, Rita Faia Marques, Daniela Massiceti, Camilla\
Longden, Linda Wen, and Edward Cutrell. 2023. Understanding Personalized\
Accessibility through Teachable AI: Designing and Evaluating Find My Things\
for People who are Blind or Low Vision. In _Proceedings of the 25th International_ _ACM SIGACCESS Conference on Computers and Accessibility_(New York, NY, USA)\
_(ASSETS ’23)_. Association for Computing Machinery, New York, NY, USA, Article\
31, 12 pages. doi:10.1145/3597638.3608395\
\[17\] Cliodhna O’Connor and Helene Joffe. 2020. Intercoder reliability in qualitative\
research: Debates and practical guidelines. _International journal of qualitative_ _methods_ 19 (2020), 1609406919899220.\
\[18\] Bianca Giulia Sarah Schor, Emma Kallina, Jatinder Singh, and Alan Blackwell.\
2024\. Meaningful Transparency for Clinicians: Operationalising HCXAI Research\
with Gynaecologists. In _Proceedings of the 2024 ACM Conference on Fairness,_ _Accountability, and Transparency_(Rio de Janeiro, Brazil) _(FAccT ’24)_. Association\
for Computing Machinery, New York, NY, USA, 1268–1281. doi:10.1145/3630106.\
3658971\
\[19\] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra. 2017. Grad-cam: Visual explanations from deep networks via gradient-based localization. In _Proceedings of the IEEE interna-_ _tional conference on computer vision_. 618–626.\
\[20\] JooYoung Seo, Sanchita S. Kamath, Aziz Zeidieh, Saairam Venkatesh, and Sean\
McCurry. 2024. MAIDR Meets AI: Exploring Multimodal LLM-Based Data Visualization Interpretation by and with Blind and Low-Vision Users. In _Proceedings of_ _the 26th International ACM SIGACCESS Conference on Computers and Accessibility_\
(St. John’s, NL, Canada) _(ASSETS ’24)_. Association for Computing Machinery,\
New York, NY, USA, Article 57, 31 pages. doi:10.1145/3663548.3675660\
\[21\] Ian René Solano-Kamaiko, Dibyendu Mishra, Nicola Dell, and Aditya Vashistha.\
2024\. Explorable Explainable AI: Improving AI Understanding for Community\
\
Health Workers in India. In _Proceedings of the 2024 CHI Conference on Human_ _Factors in Computing Systems_(Honolulu, HI, USA) _(CHI ’24)_. Association for\
Computing Machinery, New York, NY, USA, Article 399, 21 pages. doi:10.1145/\
3613904.3642733\
\[22\] Xinru Tang, Ali Abdolrahmani, Darren Gergle, and Anne Marie Piper. 2025.\
Everyday Uncertainty: How Blind People Use GenAI Tools for Information\
Access. In _Proceedings of the 2025 CHI Conference on Human Factors in Computing_ _Systems (CHI ’25)_. Association for Computing Machinery, New York, NY, USA,\
Article 63, 17 pages. doi:10.1145/3706598.3713433