---
title: "Explainability Pitfalls: Beyond Dark Patterns in Explainable AI"
source_url: "http://arxiv.org/pdf/2109.12480v1"
doi: "arXiv:2109.12480v1"
ingest_date: "2026-07-14"
status: "publish"
---

## Explainability Pitfalls: Beyond Dark Patterns in Explainable AI

Upol Ehsan & Mark O. Riedl Georgia Institute of Technology, Atlanta GA, USA {ehsanu,riedl}@gatech.edu

### Abstract

To make Explainable AI (XAI) systems trustworthy, understanding harmful effects is just as important as producing well-designed explanations. In this paper, we address an important yet unarticulated type of negative effect in XAI. We introduce explainability pitfalls (EPs), unanticipated negative downstream effects from AI explanations manifesting even when there is no intention to manipulate users. EPs are different from, yet related to, dark patterns, which are intentionally deceptive practices. We articulate the concept of EPs by demarcating it from dark patterns and highlighting the challenges arising from uncertainties around pitfalls. We situate and operationalize the concept using a case study that showcases how, despite best intentions, unsuspecting negative effects such as unwarranted trust in numerical explanations can emerge. We propose proactive and preventative strategies to address EPs at three interconnected levels: research, design, and organizational.

### 1 Introduction

Safety and trustworthiness are major goals of Explainable AI (XAI), a research area that aims to provide human-understandable justifications for the system’s behavior \[1–3\]. This safety is vital because AI systems increasingly power decision-making in high-stakes domains like healthcare \[4–7\], finance \[8, 9\], and criminal justice \[10–12\]. Adding explainabilty does not necessarily guarantee positive effects; there can also be detrimental ones. To facilitate AI safety, beyond designing effective explanations, we also need to properly understand detrimental effects of AI explanations.

Despite commendable progress in XAI, emerging work has highlighted detrimental effects of expla- nations \[13–16\]. For instance, deceptive practices can be intentionally used to design placebic expla- nations (devoid of justificatory content) and engender trust in AI systems and obfuscate harm \[17\]. However, not all detrimental effects are intentional. Despite the designer’s best intentions, it is

# arXiv:2109.12480v1 \[cs.HC\] 26 Sep 2021

possible to design explanations that have unintentional negative effects on the end-user. In such cases, what can we do? How might we conceptualize intentional negative effects of explanations? When it comes to conceptualizing negative effects of explanations, especially ones that are not intentional, there is a scarcity of conceptual artifacts.

To address this problem, we introduce the concept of explainability pitfalls (EPs), which are unanticipated and unintended negative downstream effects from AI explanations that can cause users to act against their own self-interests, align their decisions with a third party, or exploit their cognitive heuristics. Examples of these downstream negative effects include user perceptions like misplaced trust, over (or under) estimating the AI’s capabilities, and over-reliance on certain explanation forms.

Explainability pitfalls (EPs) are different from dark patterns (DPs), which are a set of deceptive practices intentionally and “carefully crafted to trick users into doing things...They do not have the user’s interests in mind” \[18\]. Emerging work showcases how dark patterns can manifest in XAI to create a false sense of security and tricking users into over-trust systems \[19\]. With roots in UX design \[20\], DPs have been explored in multiple contexts like games \[21\] and medical records \[22\]. A major difference between EPs and DPs is the difference in intentionality—DPs have bad-faith actors intentionally trying to trick users. Despite being different, EPs and DPs are related; you can
turn pitfalls into dark patterns by intentionally setting the traps (to trick the user).

We use the metaphor of “pitfalls” to signal unsuspected or hidden difficulties or dangers that are not
easily recognized. These difficulties might arise due to lack of information, understanding, or oversight (or a combination of these). Without the awareness of how to identify and avoid pitfalls, there
are increased risks for end-users who may never be aware of being affected. Moreover, explainability
pitfalls may only be symptomatic, thus detectable, after users interact with the explanations and there
is a misalignment between their behavior and designers’ expectations. This implies is a high bar of
accountability for designers to be “pitfall-aware” when designing XAI systems (at first glance, the
lack of intentionality in EPs may be misinterpreted as an exonerating force). Taking the metaphor of
pitfalls further, we can envision navigation strategies to detect and avoid them. If we are pitfall-aware
in our navigation of the design space and aware of the possibility of unanticipated and unintentional
negative effects, we can proactively build resilience against the pitfalls.
The motivation for conceptualizing EPs is not purely theoretical or speculative. It is practically

The motivation for conceptualizing EPs is not purely theoretical or speculative. It is practically
motivated and empirically situated in our prior work \[23\] that (amongst other things) showcased how,
despite no intentions to trick anyone, unsuspecting negative effects can emerge from interpretations of
AI explanations. The conceptual introduction of explainability pitfalls aims to (1) bring awareness to
previously unrealized intellectual blind spots (around negative effects of AI explanations), which, in
turn, can (2) expand the XAI design space. This paper is not a comprehensive treatise of EPs; rather,
it takes a foundational step towards operationalizing the notion both conceptually and practically.

Below we operationalize the concept of EPs by situating it through a case study where EPs manifested
and were discovered through qualitative analysis of end-user responses to explanations in a controlled
setting. Reflecting on the findings, we then propose formative strategies to address EPs.

2 Case Study: Situating Explainability Pitfalls

In this case study \[23\], we investigated how two different groups—people with and without a
background in AI—perceive different types of AI explanations. We probed for user perceptions on
three types of AI-generated explanations: (1) natural language with justification, (2) natural language
without justification, and (3) numbers that provide uncontextualized transparency into agent’s actions.
For our purposes to situate the notion of EPs, we need to focus on how and why both groups reacted
to the numbers from the Numerical-Reasoning (NR) robot (#3).

In the study, participants provided both qualitative and quantitative perception information after watching videos of three
robots (AI agents) using Reinforcement Learning to navigate
a sequential decision-making environment—a field of rolling
boulders and flowing lava to retrieve essential food supplies for
trapped space explorers (more task details in \[23\]). The robots
behave identically except in the way they “think out loud” or
explain themselves. The NR robot (the relevant one for this
paper) “thinks out loud” by simply outputting the numerical Qvalues for the current state (Fig. 1). Q-values \[24\] can provide
some transparency into the agent’s beliefs about each action’s
relative utility (“quality”), but do not contain information on
“why” one action has a higher utility than another. Participants
were not told that the numbers are Q-values nor do they know
which values correspond to which actions.

For the AI group, the mere presence of numbers triggered heuristic reasoning that associated mathematical representations with logical algorithmic thinking process even when they could “‘not fully

“why” one action has a higher utility than another. Participants \[Image: Im1\]
were not told that the numbers are Q-values nor do they know Figure 1: Screenshot depicting the
Numerical-Reasoning (NR) robot navigating the task environment and “think-
We found that participants in both groups had unwarranted
ing out loud” using numbers. Taken
faith in numbers. However, their extent and reasons for doing
from \[23\]. This robot was used as a foil
so were different. To understand the reasons behind the effect,
against two other robots with natural
we will use the notion of cognitive heuristics (rules-of-thumb or language explanation strategies.
mental short-cuts), which leads to biases and errors if applied understand the logic behind \[NR’s\] decision making.’ (A43)” \[23\]. Contradictorily, they voted the least understandable robot (NR) to be more intelligent! To them, “‘Math \[...had\] an aura of intelligence’, which ‘made the NR robot feel smarter’ (A16, A75)” \[23\]. Not only did they over-value numerical representation, but this group also viewed numbers as potentially actionable even when their meaning was unclear. Actionability refers to what one might do with the information in terms of diagnosis or predicting future behavior. Many highlighted that even if they could not ‘make sense of numbers right now, \[they\] should be able to act on them in the future’ (A39)” \[23\]. But how actionable were NR’s numbers in actuality? As we highlighted before, Q-values cannot indicate the “why” behind the decision. These numbers do not allow much actionability beyond an assessment of the quality of the actions available. That is, despite a desire to correct errors, having the numbers on hand would not help them determine the cause of failures that could be corrected. Instead, they engendered over-trust and misplaced assessment of the robot’s intelligence.

For the non-AI group, the very inability to understand complex numbers triggered heuristic reasoning that NR must be intelligent. NR’s “‘language of numbers’, because of its ‘cryptic incomprehensibil- ity’, signaled intelligence (NA6, NA1)” \[23\]. Note that this line of reasoning is different from the AI group’s heuristic which posited a future actionability (despite present lack of understandability).

Operationalizing the concept of EPs, our case study showcases how even when there is no intention to deceive, unsuspected effects (i.e., over-reliance on numbers) can arise. For either group, we did not anticipate that unlabeled, seemingly incomprehensible numbers would increase trust and assessment of the agent’s intelligence. Moreover, we presented the Q-values in good-faith. What if these numbers were manipulated? Imagine bad-faith actions exploiting these pitfalls to manifest dark patterns. For instance, an XAI system that explains in (manipulated) numbers (to induce trust); given the heuristic faith in numbers, it can induce over-trust and incorrect perceptions of the system.

# 3 Navigation Strategies for Explainability Pitfalls

Given their nature, it is unlikely that we can completely eliminate explainability pitfalls (EPs). Recall the uncertainty around EPs— just because they exist does not guarantee the downstream harms will happen. We do not yet know enough to predict when, how, and why a given AI explanation will trigger unanticipated negative downstream effects. While we are vulnerable to pitfalls and there is no silver bullet solution, we can increase our resiliency by adopting pitfall-aware strategies—proactive and preventative measures that help us understand where pitfalls tend to be found, how they work, and how they can be avoided. To expand on the pitfall metaphor, we want to probe the areas (“grounds”) of the explanation design space (where pitfalls are likely to occur) to increase our likelihood of being on sturdy ground. We can be pitfall-aware (proactive and preventative) in our approaches at three interconnected levels: research, design, and organizational.

At the research level, we need to conduct more situated and empirically diverse human-centered research to obtain a refined understanding of the stakeholders as well as the dimensions of explanations that affect different stakeholders in XAI. This is because pitfalls become symptomatic—and thereby identifiable—when downstream effects (like user perceptions on AI explanations) manifest. For instance, the case study in Section 2 revealed that different AI backgrounds in end-users can trigger the same pitfall (over-trust in numbers) but for different heuristic reasons. Without running the study, we could not have identified these pitfalls. Fortunately, the case study was a controlled lab experiment and not a real-world deployment, which limits the potential harm done by EPs. However, the exploration in the case study revealed an important blind spot around the divergent interpretations of explanations based on one’s AI background. Building on these insights, we can do further research on a range of relevant areas. For instance, how combinations of user characteristics (e.g., educational and professional backgrounds) impact susceptibility to EPs, how different heuristics can combine to manifest harmful biases, and how different users appropriate explanations in unexpected manners. Taking a pitfall-aware mindset in these explorations can generate actionable insights about how end-user reactions to AI explanations may diverge from designer intentions.

At the design level, we seek design strategies that are resilient to pitfalls. One possible strategy can be to shift our explanation design philosophy to emphasize user reflection (as opposed to acceptance) during interpretation of explanations. Recent human-centered XAI work has also advocated for conceptualizing ways to foster trust via reflection \[28\]. In terms of origins, some pitfalls are a consequence of uncritical acceptance of explanations. Langer et al. \[29\] point out that people are likely to accept explanations without conscious attention if no effortful thinking is required from them. In Kahneman’s dual-process theory \[25\] terms, this means that if we do not
invoke mindful and deliberative (system 2) thinking with explanations, we increase the likelihood of
uncritical consumption. To trigger mindfulness, Langer et al. \[29\] recommend to design for “effortful
responses” or “thoughtful responding”. To help with mindfulness, we can incorporate the lenses
of seamful design \[30\], which emphasize configurability, agency, appropriation, and revelation of
complexity \[31\]. Seamful design is the complement of the notion of "seamlessness" in computing
systems (cf. \[30–32\]) and has conceptual roots in Ubiquitous Computing \[30\].

The notion of seamfulness aligns well with XAI because (a) AI systems are deployed in what
Vertesi calls seamful spaces \[33\], and (b) the approach can be viewed as a response to “seamless”
black-boxed AI decisions with “zero friction” or understanding. In terms of form and function,
seams strategically reveal complexities and mechanisms of connection between different parts while
concealing distracting elements. This notion of “strategic revealing and concealment” is central to
seamful design because it connects form with function \[31\]. Understanding of such connections can
promote reflective thinking \[30\]. Seamful explanations, thus, strategically reveal relevant information
that augment system understanding and conceal those that distract. They shed light on both the
imperfections and affordances of the system, awareness of which can add useful cognitive friction
and promote effortful and reflective thinking. Examples of seamful explanations include interactive
counterfactual explanations where we prompt the user with what-if scenarios. For instance, what if
the AI group members were prompted to reflect using counterfactual scenarios on Q-values? Making
the counterfactuals explicit can help the user to be aware of the variability around the system’s
decision, which can help build better mental models of the system \[34\]. Moreover, by facilitating
contrastive thinking, counterfactuals elicit engagement and deliberative thinking \[35\], which can
potentially help navigate around EPs.
At an organizational level, we can introduce educational (training) programs (e.g., pitfall literacy

At an organizational level, we can introduce educational (training) programs (e.g., pitfall literacy
programs) for both designers and end-users. Having an ecosystem perspective is important because
EPs have sociotechnical complexities; thus, we need strategies beyond the technical level. Recent
work has shown that literacy of dark patterns can promote self-reflection and mitigate harms \[36\].
We can develop EP literacy programs that can (a) help designers become aware of how EPs might
manifest and (b) empower end-users to identify being trapped in pitfalls. These programs can
include simulation exercises using the methodological lenses of speculative design \[37\] and reflective
design \[38\] to envision “what could go wrong” \[39\] in facets of XAI systems. Designers can use
participatory design \[40\] with end-users to gather effects of potential EPs. They can also utilize
case studies (like ours) to think through the effects of the pitfalls. Insights from these programs can
facilitate the navigation around pitfalls at both the design and evaluation levels of the ecosystem.
Taken together, these pitfall-aware strategies help us address EPs in a proactive and preventative

Taken together, these pitfall-aware strategies help us address EPs in a proactive and preventative
manner, fostering resiliency against pitfalls. These strategies are neither exhaustive nor normative,
but take a formative step towards practically addressing the potential harmful of EPs.

However, there are a number of open research questions, some of which we enumerate here:

Being able to appropriately classify negative impacts of AI explanations is crucial to making XAI
systems safe and reliable. By starting the conversation about explainability pitfalls (EPs), this paper
brings conscious awareness to the (previously unarticulated) possibility of unintended negative effects
of AI explanations. By broadening the scope of harmful effects in XAI, EPs expand the dialogue
that has already started around dark patterns. The operationalization of EPs and proposed mitigation
strategies provide actionable insights that can improve accountability and safety in XAI systems.
However, there are a number of open research questions, some of which we enumerate here:

4 Concluding Reflections

3.How might we assess the impact of training programs to mitigate the effects of pitfalls?

We seek to learn from and with the HCI and AI communities through foundational and applied
research to further develop the conceptual and practical facets of explainability pitfalls. We believe
that further understanding of where, how, and why unintended pitfalls reside in the design space of
XAI can lead to improved safety and user empowerment in AI systems.

* * *

# Acknowledgments

With our deepest gratitude, we thank our participants for generously investing their time in the case study. We are grateful to Zhiyu Lin, Sarah Wiegreffe, Amal Alabdulkarim, Becky Peng, and Kaige Xie for their feedback on the ideas. We are indebted to Samir Passi, Vera Liao, Larry Chan, Ethan Lee, and Michael Muller for their contributions to the case study, which informed the current work. Special thanks to Rachel Urban for generously providing proofreading feedback. This project was partially supported by the National Science Foundation under Grant No. 1928586.

# References

\[1\] Amina Adadi and Mohammed Berrada. Peeking inside the black-box: A survey on explainable artificial intelligence (xai). IEEE Access, 6:52138–52160, 2018.

\[2\] Upol Ehsan, Pradyumna Tambwekar, Larry Chan, Brent Harrison, and Mark Riedl. Automated rationale generation: A technique for explainable ai and its effects on human perceptions. In Proceedings of the International Conference on Intelligence User Interfaces, 03 2019.

\[3\] Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. A survey of methods for explaining black box models. ACM computing surveys (CSUR), 51(5):1–42, 2018.

\[4\] Andreas Holzinger, Chris Biemann, Constantinos S Pattichis, and Douglas B Kell. What do we need to build explainable ai systems for the medical domain? arXiv preprint arXiv:1712.09923,

\[5\] Gajendra Jung Katuwal and Robert Chen. Machine learning model interpretability for precision medicine. arXiv preprint arXiv:1610.09045, 2016.

\[6\] Zhengping Che, Sanjay Purushotham, Robinder Khemani, and Yan Liu. Interpretable deep models for icu outcome prediction. In AMIA Annual Symposium Proceedings, volume 2016, page 371. American Medical Informatics Association, 2016.

\[7\] Tyler J. Loftus, Patrick J. Tighe, Amanda C. Filiberto, Philip A. Efron, Scott C. Brakenridge, Ali- cia M. Mohr, Parisa Rashidi, Jr Upchurch, Gilbert R., and Azra Bihorac. Artificial Intelligence and Surgical Decision-making. JAMA Surgery, 155(2):148–158, 02 2020.

\[8\] Donald MacKenzie. Material Signals: A Historical Sociology of High-Frequency Trading. American Journal of Sociology, 123(6):1635–1683, 2018.

\[9\] John Murawski. Mortgage providers look to ai to process home loans faster. Wall Street Journal, March 2019.

\[10\] Cynthia Rudin, Caroline Wang, and Beau Coker. The age of secrecy and un- fairness in recidivism prediction. Harvard Data Science Review, 2(1), 3 2020. [https://hdsr.mitpress.mit.edu/pub/7z10o269](https://hdsr.mitpress.mit.edu/pub/7z10o269).

\[11\] Jon Kleinberg, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, and Sendhil Mullainathan. Human Decisions and Machine Predictions. The Quarterly Journal of Economics, 133(1):237– 293, 2017.

\[12\] Karen Hao. Ai is sending people to jail – and getting it wrong. MIT Technology Review, January

\[13\] Simone Stumpf, Adrian Bussone, and Dympna O’sullivan. Explanations considered harmful? user interactions with machine learning systems. In ACM SIGCHI Workshop on Human- Centered Machine Learning, 2016.

\[14\] Alison Smith-Renner, Ron Fan, Melissa Birchfield, Tongshuang Wu, Jordan Boyd-Graber, Daniel S Weld, and Leah Findlater. No explainability without accountability: An empirical study of explanations and feedback in interactive ml. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, pages 1–13, 2020.

* * *

\[15\]Harmanpreet Kaur, Harsha Nori, Samuel Jenkins, Rich Caruana, Hanna Wallach, and Jennifer Wortman Vaughan. Interpreting Interpretability: Understanding Data Scientists’ Use of Inter- pretability Tools for Machine Learning. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, CHI ’20, pages 1–14, New York, NY, USA, 2020. Association for Computing Machinery.

\[16\] Bhavya Ghai, Q Vera Liao, Yunfeng Zhang, Rachel Bellamy, and Klaus Mueller. Explainable active learning (xal) toward ai explanations as interfaces for machine teachers. Proceedings of the ACM on Human-Computer Interaction, 4(CSCW3):1–28, 2021.

\[17\] Malin Eiband, Daniel Buschek, Alexander Kremer, and Heinrich Hussmann. The Impact of Placebic Explanations on Trust in Intelligent Systems. In Extended Abstracts of the 2019 CHI Conference on Human Factors in Computing Systems, CHI EA ’19, pages 1–6, New York, NY, USA, 2019. Association for Computing Machinery.

\[18\] Harry Brignull, Marc Miquel, Jeremy Rosenberg, and James Offer. Dark patterns-user interfaces designed to trick people, 2015.

\[19\] Michael Chromik, Malin Eiband, Sarah Theres Völkel, and Daniel Buschek. Dark patterns of explainability, transparency, and user control for intelligent systems. In IUI workshops, volume 2327, 2019.

\[20\] Colin M Gray, Yubo Kou, Bryan Battles, Joseph Hoggatt, and Austin L Toombs. The dark (patterns) side of ux design. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, pages 1–14, 2018.

\[21\] José P Zagal, Staffan Björk, and Chris Lewis. Dark patterns in the design of games. In Foundations of Digital Games 2013, 2013.

\[22\] Daniel Capurro and Eduardo Velloso. Dark patterns, electronic medical records, and the opioid epidemic. arXiv preprint arXiv:2105.08870, 2021.

\[23\] Upol Ehsan, Samir Passi, Q Vera Liao, Larry Chan, I Lee, Michael Muller, Mark O Riedl, et al. The who in explainable ai: How ai background shapes perceptions of ai explanations. arXiv preprint arXiv:2107.13509, 2021.

\[24\] Christopher JCH Watkins and Peter Dayan. Q-learning. Machine learning, 8(3-4):279–292,

\[25\]Daniel Kahneman. Thinking, fast and slow. Macmillan, 2011.

\[26\] Peter C Wason and J St BT Evans. Dual processes in reasoning? Cognition, 3(2):141–154,

\[27\] Richard E Petty and John T Cacioppo. The elaboration likelihood model of persuasion. In Communication and persuasion, pages 1–24. Springer, 1986.

\[28\] Upol Ehsan and Mark O Riedl. Human-centered explainable ai: Towards a reflective sociotech- nical approach. In International Conference on Human-Computer Interaction, pages 449–466. Springer, 2020.

\[29\] Ellen J Langer, Arthur Blank, and Benzion Chanowitz. The mindlessness of ostensibly thought- ful action: The role of" placebic" information in interpersonal interaction. Journal of personality and social psychology, 36(6):635, 1978.

\[30\] Matthew Chalmers and Ian MacColl. Seamful and seamless design in ubiquitous computing. In Workshop at the crossroads: The interaction of HCI and systems issues in UbiComp, volume 8,

\[31\] Sarah Inman and David Ribes. " beautiful seams" strategic revelations and concealments. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, pages 1–14,

\[32\] Gregor Broll and Steve Benford. Seamful design for location-based mobile games. In Interna- tional Conference on Entertainment Computing, pages 155–166. Springer, 2005.

* * *

\[33\] Janet Vertesi. Seamful spaces: Heterogeneous infrastructures in interaction. Science, Technology, & Human Values, 39(2):264–284, 2014.

\[34\] Tim Miller. Explanation in artificial intelligence: Insights from the social sciences. Artificial Intelligence, 267:1–38, 2019.

\[35\] Ruth MJ Byrne. Counterfactuals in explainable artificial intelligence (xai): Evidence from human reasoning. In IJCAI, pages 6276–6282, 2019.

\[36\]Jonathan Magnusson. Improving dark pattern literacy of end users.

\[37\] James Auger. Speculative design: crafting the speculation. Digital Creativity, 24(1):11–35,

\[38\] Phoebe Sengers, Kirsten Boehner, Shay David, and Joseph’Jofish’ Kaye. Reflective design. In Proceedings of the 4th decennial conference on Critical computing: between sense and sensibility, pages 49–58, 2005.

\[39\] Lucas Colusso, Cynthia L Bennett, Pari Gabriel, and Daniela K Rosner. Design and diversity? speculations on what could go wrong. In Proceedings of the 2019 on Designing Interactive Systems Conference, pages 1405–1413, 2019.

\[40\] Michael J Muller and Sarah Kuhn. Participatory design. Communications of the ACM, 36(6):24– 28, 1993.