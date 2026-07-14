---
title: "Explainable AI for Data-Driven Design of High-Dimensional Predictive Studies"
source_url: "http://arxiv.org/pdf/2605.22243v1"
doi: ""
ingest_date: "2026-07-14"
status: "publish"
---

# Explainable AI for Data-Driven Design of High-Dimensional Predictive Studies

\*1,2,3 \*1,2 1,2 1,2
**Junyu Yan, Damian Machlanski, Kurt Butler, Panagiotis Dimitrakopoulos, Ewen M**
1,2
**Harrison⁴, Bruce Guthrie³, Sotirios A Tsaftaris**

1. School of Engineering, University of Edinburgh, Edinburgh, UK

2. Causality in Healthcare AI Hub (CHAI), UK

3. Causality in Healthcare AI Hub (CHAI), UK

4. Advanced Care Research Centre, Usher School of Population Health Sciences, University of

5. Advanced Care Research Centre, Usher School of Population Health Sciences, University of
   Edinburgh, Edinburgh, UK

6. Centre for Medical Informatics, Usher School of Population Health Sciences, University of

7. Centre for Medical Informatics, Usher School of Population Health Sciences, University of
   Edinburgh, Edinburgh, UK


Corresponding Author: Damian Machlanski ( [d.machlanski@ed.ac.uk](mailto:d.machlanski@ed.ac.uk))

## Abstract

Predictive modelling is important for health data analysis and data-driven clinical decision-making.
However, predictive studies are challenging to design optimally by hand when tens or even hundreds
of features require selection, transformation, or interaction modelling. While complex machine learning
models offer high performance, their "black-box" nature limits the clinical trust, transparency, and
interpretability required for decision-making. We developed and evaluated an Exploratory AI
Recommender that provides data-driven recommendations to improve predictive performance of
existing interpretable statistical models. The developed framework uses flexible AI modelling to
capture complex data patterns and explainable AI techniques to translate the patterns into three
recommendation types: feature exclusion, non-linear terms, and feature interactions. We evaluated the
framework by comparing predictive performance of a baseline (i.e., no interactions or non-linear terms)
Cox Proportional Hazards (CPH) model against an augmented CPH incorporating recommendations
suggested by our method. The primary analysis predicts the time to the first occurrence of a fall or
related injury in 245,614 patients. Our method recommended excluding 23 features, including nonlinear terms for two features, and including 221 suggested feature interactions. The C-index improved
from 0.805 (95% CI 0.798-0.812) to 0.815 (95% CI 0.809-0.822), and so did calibration (intercept: -
0.006 to 0.003; slope: 1.063 to 0.950). All recommendations were supported by existing literature. The
method also proved effective on two additional public datasets, demonstrating wider applicability. The
proposed Exploratory AI Recommender demonstrates the potential of explainable AI and data-driven
study design to improve the process of developing, and the performance of high-dimensional
transparent predictive models.

\*
The two authors contributed equally.

* * *

## Introduction

Predictive modelling is important in healthcare as it enables proactive clinical decisions by forecasting
future health outcomes from patient data. A prime example is models for predicting 10-year
2
cardiovascular risk including PREVENT¹ and QRISK, which support clinician and patient decisionmaking about initiation of preventive medications. Historically, clinical predictive modelling has been
the domain of standard statistical methods. Techniques such as Cox Proportional Hazards (CPH) have
3,4
served medical research for decades. They are computationally efficient, mathematically rigorous,
and, crucially, intrinsically interpretable.

However, as the dimensionality (i.e., number of variables) of healthcare data increased (e.g., electronic
healthcare records), the limitations of these classical approaches have become increasingly apparent.
Standard statistical methods, while trustworthy, often rely on linearity assumptions that may not reflect
biological reality. In clinical practice, the risk factor-outcome relationship is rarely a straight line. For
instance, the risk associated with body mass index or blood pressure may follow a U-shaped curve (i.e.,
non-linearity), or the impact of a specific biomarker may be additionally dependent on a patient’s age
or genetic profile (i.e., interaction). Capturing these nuances through “feature engineering”, the manual
process of transforming variables and specifying interactions, becomes intractable as data grows. For
example, with only 100 features, the number of two-way interactions reaches 4 950 possibilities,
making it nearly impossible for researchers to manually identify every clinically relevant synergy.

Modern Artificial Intelligence (AI) predictors have demonstrated the capacity to outperform classical
5
approaches in a variety of clinical tasks. These models excel at "end-to-end learning," where the model
learns expressive feature representations directly from raw data without the need for manual feature
6,7
engineering. This allows AI models to capture non-linearities and high-order interactions that would
be invisible to standard techniques. However, this performance gain comes at a significant cost: the loss
of clinical “sense-checking”. When a model functions as a “black-box”, clinicians cannot verify if a
8
prediction is based on sound pathophysiology or mere statistical noise and “shortcuts” in the dataset.
While some argue that high predictive performance should take precedence over interpretability in
9,10
clinical AI, this lack of transparency prevents clinicians from explaining _why_ a patient is at risk,
hindering the ability to identify high-risk profiles that warrant further clinical investigation and
11–13
undermining the trust required for clinical adoption in high-stakes environments.

14
To address the black-box problem, the field of explainable AI has emerged. One line of explainable
AI research is on attribution, the process of assigning “credit” to input features for a model’s prediction
15
using methods like SHAP (SHapley Additive exPlanations). Explainable AI methods have been
16–19 20,21
successfully used to analyze risk predictors, to identify biomarkers in diseases, or factors in
22,23
cardiovascular risk.

This study explores the potential of explainable AI not merely as a tool for post-hoc justification of
black-box predictions, but as a mechanism to design better white-box models, a process we refer to as
data-driven study design. While previous work investigated automated feature engineering with simple
24 25
models, and augmented Cox models with explainable AI-derived new predictors, it remains unclear
whether explainable AI can automate all three feature engineering tasks (feature selection, non-linear
terms, interaction terms) to improve the performance of conventional clinical models on highdimensional health data. Our method aims to bridge this gap by gaining predictive strength of complex
AI models while retaining the simplicity of conventional predictors. By using explainable AI to
“discover” the complex relationships and then embedding them back into transparent statistical tools, we provide clinicians with a model that is as powerful as modern AI but as auditable as a standard risk
score.

## Methods

Our study proposes an Explainable AI-based Exploratory AI Recommender ( _Recommender_ henceforth)
designed to systematically uncover inherent data relationships and optimize the design of predictive
cohort studies. The methodology follows three stages (Figure 1): (1) establishing a baseline predictive
model, representing the initial analytic stage of a research team; (2) deploying our Recommender to
generate actionable insights and recommendations for refining study design; and (3) evaluating the
Recommender’s utility by quantifying performance gains of models augmented with these
recommendations. We apply this methodology to a clinical case study: predicting the risk of falls or
related injuries (FRI) using DataLoch data.

## Data Source and Study Population

The analysis was conducted on a high-dimensional clinical dataset provided by Lothian DataLoch, a
26
secure, regional data repository linking primary and secondary care data in South East Scotland. This
study included all individuals aged over 50 years, permanently registered for at least one year with a
Lothian General Medical Practice (GP) that contributes to the DataLoch dataset in the period
01/01/2015-28/02/2020. This pre-COVID-19 period was specifically chosen to mitigate potential biases
on FRI that might arise from pandemic-related changes in healthcare-seeking behavior. Individuals
were excluded if data for age, sex, or the index of multiple deprivation were missing. Patients left the
cohort at the earliest of death, GP de-registration, an outcome event, or the study end date (February
28, 2020). The dataset was randomly split into 80% training ( ~~196 491 rows) and 20% held-out test
data (~~ 49 123 rows). This study follows the Transparent Reporting of a Multivariable Prediction Model
27
for Individual Prognosis or Diagnosis (TRIPOD+AI) reporting guidelines.

## Outcomes The primary outcome was the time from cohort entry to the first occurrence of FRI, where related

The primary outcome was the time from cohort entry to the first occurrence of FRI, where related
injuries were defined as low energy fractures (hip, wrist, and proximal humerus). Diagnosis of FRI was
defined by clinical codes from primary care (Read version 2), hospital admissions (ICD-10), and
emergency department records (Supplementary Table 1).

## Design, Implementation and Evaluation of the Exploratory AI Recommender

First, we established a baseline predictive model using the standard multivariable Cox Proportional
Hazards model. This model represents the starting point of a conventional, literature-driven predictive
modeling study. Following the knowledge-driven approach, we selected 58 predictors from
approximately 400 available features based on established literature. These include four patient
demographic characteristics, three lifestyle risk factors, 27 comorbidities, electronic Frailty Index
28
category, and exposure to 23 Fall-Risk-Increasing Drugs (list of features in Supplementary Table 4;
see Supplementary Note 1 for further details). The baseline model was fitted on the training data using
all 58 candidate predictors, deliberately omitting advanced techniques such as feature selection, nonlinear terms, or interaction terms. Its performance on the held-out test set served as the baseline for
evaluating Recommender-driven refinements.

* * *

linear relationships and potential interactions between all features and outcomes. For this purpose, we
employed Random Survival Forest²⁹ (RSF) as the exploratory AI model. Unlike typical machine
learning applications, the RSF was used purely to capture high-dimensional data structures rather than
for final clinical prediction. Next, the RSF model was interpreted using explainable AI techniques, such
15
as SHAP, to translate “black-box” patterns into actionable insights. SHAP quantifies each feature’s
contribution (termed _feature attributions_ (FAs)) to the RSF’s prediction for each patient (see
Supplementary Note 2). Standard FA analysis often relies on population level averaging, which can
obscure risk factors that are clinically significant only within specific subgroups. To resolve this, we
performed an extreme-group FA analysis that targets two distinct risk cohorts: a low-risk and high-risk
cohort. The low-risk cohort included individuals with RSF predicted risk within a predefined margin
(Euclidean distance < 0.05 times SD of the model’s predictions) of the mean score for patients with no
FRI events. The high-risk cohort was similarly defined relative to the mean score for patients with a fall
event. The FAs from these cohorts were then processed to derive modeling recommendations. While
computing FAs might be more intensive on average than training a baseline Cox model, this exploratory
phase is a one-time cost that precedes the deployment of the more efficient augmented model.

Our Recommender offers the following three types of recommendations (Figure 2): (1) **Feature** **exclusion (Figure 2; E).** A feature was recommended for exclusion if the upper bound of the 95% CI
of its mean absolute FA did not exceed a data-driven significance threshold. The threshold was defined
as 5% of the standard deviation of mean absolute FA values across all candidate features, a heuristic to
distinguish features with negligible contributions; (2) **Non-linear relationships (Figure 2; D).** We
calculated the Pearson correlation coefficient 𝑟 between the feature values and their corresponding FAs
for each feature. For any feature with a weak correlation (\|𝑟\| < 0.1), we recommended modelling its
effect using non-linear terms (e.g., quadratic terms, splines); (3) **Feature interactions (Figure 2; A-** **C).** We employed an iterative stratification analysis on FAs to identify potential feature interactions,
guided by three types of data patterns (see Figure 2) **.** Once stratified, FAs were produced for each
stratum (i.e., Step 2 above repeated for each stratum). A Wilcoxon rank-sum test was then employed to
compare FA distributions between created strata. Statistically significant differences indicated a
recommendation to include a first-order (i.e., two-way) interaction term between the stratifying feature
and the statistically different features.

Third, we evaluated the effectiveness of the Recommender. We constructed augmented Cox models
that integrated these recommendations (excluding features, adding non-linear terms and interactions).
We then compared the predictive performance of these augmented models against the baseline on the
held-out test set. Furthermore, the clinical plausibility of all generated recommendations was validated
by reviewing existing medical literature.
Application to Other Datasets

## Application to Other Datasets

To establish the broader applicability and robustness of our method, we applied the Recommender on

_German Breast Cancer Study Group 2 (GBSG2)_. The data comes from a randomized clinical trial that
compared different chemotherapy treatment regimens and their effects on survival in breast cancer
patients. This study group consists of 686 samples and 8 features with a 43.6% survival rate. The
features include: age, estrogen receptor level (estrec), the number of positive (involved) lymph node
(pnodes), progesterone receptor level (progrec), hormonal therapy (horTh), tumour grade (tgrade),
menopausal status (menostat), tumor size (tsize).

* * *

_AIDS Clinical Trial (ACT)_. This data set contains 1151 HIV-positive patients from a randomized
controlled trial that compared different drug regimens. The data set includes 11 features: treatment
indictor (tx), treatment group indicator (txgrp), CD4 stratum at screening (strat2), sex, race/ethnicity
(raceth), IV drug use history (ivdrug), hemophiliac (hemophil), Karnofsky Performance Scale (karnof),
Baseline CD4 count (cd4), Months of prior ZDV use (priorzdv), and age. The endpoint was time to an
AIDS-defining event or death, with a censoring rate of 89.4%.

1
All data sets were accessed via the scikit-survival Python library. For each data set, the cohort was
randomly split into a training set (80%) and a test set (20%). The complete Explainable AI-based
Exploratory AI Recommender workflow, including fitting a baseline Cox model, training an
exploratory (RSF) model with 1000 trees, and applying SHAP to derive recommendations, was
performed in the same way as for the primary dataset.

## Statistics and Reproducibility Baseline characteristics of study samples were described using frequency and percentage, mean and

Baseline characteristics of study samples were described using frequency and percentage, mean and
standard deviation (SD). Statistical analyses, model development, and testing were conducted in Python,
version 3.12.5. All model performances (i.e., baseline CPH, RSF, and augmented CPH) were quantified
by the concordance index (C-index) for discrimination and calibration plots for calibration (intercept
and slope). All confidence intervals were 95% percentile intervals generated using 1000 bootstraps. All
tests were 2-tailed, and P < 0.05 was considered as significant.

## Study Approval and Consent

All data from DataLoch were linked and de-identified by the DataLoch service (Edinburgh, United
Kingdom) and analyzed within a Secure Data Environment (reference: DL\_2024\_030). DataLoch
enables access to de-identified extracts of healthcare data from the South-East Scotland region to
approved applicants: [https://dataloch.org/](https://dataloch.org/). The study was reviewed and received approval under
delegated authority from a regional National Health Service Research Ethics Committee (REC
22/NS/0093) and Caldicott Guardian. Individual patient consent was not required. Clinical trial number:
not applicable.

## Results

114 067 (46.4%) females, of whom 891 (0.4%) self-identified as Black, 3444 (1.4%) as Asian, and
207 254 (84.4%) as White. The most prescribed medications were opioid analgesics (188 237 patients
\[76.7%\]), non-steroidal anti-inflammatory drugs (71 078 patients \[28.9%\]) and angiotensin-converting
enzyme inhibitors (66 644 patients \[27.1%\]), while the most prevalent comorbidities were hypertension

## Baseline Performance

The baseline CPH achieved a C-index of 0.805 (95% CI 0.798-0.812) with a calibration slope of 1.063
and intercept of -0.006 on the test set (Figure 3; A). The exploratory RSF model achieved a C-index of
0.820 (95% CI 0.813-0.827) with a calibration slope of 1.142 and intercept of -0.014 (Figure 3; B). The
discriminative and well-calibrated performance demonstrated the ability of the exploratory model to
capture complex relationships between features.

1[https://scikit-survival.readthedocs.io/en/stable/api/datasets.html](https://scikit-survival.readthedocs.io/en/stable/api/datasets.html)

* * *

## Generated Recommendations Figure 4 and Figure 5 detail the process for conducting FA analysis and deriving recommendations. The

Figure 4 and Figure 5 detail the process for conducting FA analysis and deriving recommendations. The
fall risk scores (derived from the RSF model) and pre-defined margins were used to select low-risk and
high-risk cohorts. As a result, 6928 and 2362 patients were selected into the low-risk and high-risk
cohort respectively from the initial training set (~196 491 rows). The FA analysis was conducted on
these two cohorts separately (Figure 4). This analysis generated several recommendations for model
refinement. First, it recommended 22 features for exclusion as their contributions were not significant
either in the high-risk or low-risk cohort (Supplementary Figure 1). Second, within the remaining 36
features, it identified two features with a weak correlation between FAs and feature values (low-risk
cohort: alcohol status (\|𝑟\| = -0.03 (P=.29)); high-risk cohort: alcohol status (\|𝑟\| = -0.10 (P=.11)), age
(\|𝑟\| = 0.01 (P=.86))). These features were recommended as non-linear terms in further modeling.
Finally, the analysis identified 221 first-order interactions through stratification on 10 variables (e.g.,
age, loop diuretics, dementia) following three data stratification patterns (Supplementary Figure 1).
Take age as an example, age demonstrated a wide range of FAs; below a certain feature value, it
contributed negatively to FRI risks, whereas above that value, it contributed positively. Consequently,
age was stratified by feature values to illustrate interactions with other features. Figure 5 shows agestratified results within the low-risk cohort using a 65-year cutoff (a conventional threshold for older
age group and close to the mean age at which FA ≈ 0). 2362 patients were aged under 65, and 4566
were over 65. Several features have significantly different FA distributions between two age strata,
particularly in opposing directions (e.g., antipsychotic drugs, stroke). These results suggest that the
effects of these factors on FRI risk are modified by age, illustrating their interactions. The identified
interactions were recommended as multiplicative terms between the stratified feature and its
corresponding interacted features in the further augmented model.

$$
(\|r\|=\_00.03\ (tt\\mathrm P{{=}29}))
$$

$$
(\|r\|=\_0.10;(\\mathrm{P=.11}))
$$

$$
(\|r\|=0.01~(\\mathrm{P{{=}86}})))
$$

$$
\\mathrm{F A}\\approx0\]
$$

## Quantitative Evaluation of Recommendations

We integrated the three types of recommendations into augmented Cox models independently and
cumulatively to evaluate their individual and collective impact (Figure 3). **Independent assessment.**
An augmented CPH model incorporating only the feature exclusion recommendations (58 features
reduced to 36) demonstrated no degradation in performance compared with the baseline CPH model
(∆C-index, -0.001 (95% CI -0.002-0.000), p=.10). A CPH model incorporating quadratic terms for the
three identified non-linear features on top of 58 baseline features achieved a C-index of 0.805 (95% CI,
0.798-0.812) and calibration (slope, 1.063; intercept, -0.005), which slightly improved against the
baseline model. An augmented CPH model adding the 221 recommended first-order interactions to the
58 baseline predictors (i.e., no feature exclusion) demonstrated a significant improvement over the
baseline model (C-index, 0.811 \[95% CI, 0.804-0.818\]; ΔC-index, 0.006 \[95% CI, 0.004-0.009\]; P <
0.001) and better calibration (slope, 0.966; intercept, 0.001). **Cumulative assessment.** The final CPH
model, incorporating all 3 types of recommendations (first feature exclusion, then non-linear and
interaction terms), achieved a C-index of 0.815 (95% CI, 0.809-0.822) and a calibration slope of 0.950
with an intercept of 0.003. Compared with the baseline CPH model, the final model showed a significant
improvement in discrimination (ΔC-index, 0.010; 95% CI, 0.008-0.013; P < 0.001) and calibration.
**Evaluation of Recommendations on Other Datasets**

## Evaluation of Recommendations on Other Datasets

The Recommender generated actionable recommendations that led to significant model performance
improvements on two additional datasets (Figure 6 and Figure 7).

**GBSG2**. The baseline Cox model achieved a C-index of 0.665 (95% CI 0.665 – 0.665) on the test set,
with a calibration slope of 0.963 and an intercept of 0.106. The corresponding RSF model achieved a

* * *

C-index of 0.673 (95% CI 0.673-0.673) with the calibration slope of 1.163 and intercept of -0.004
(Figure 6; B).

The feature attribution analysis (Figure 6; A) produced the following recommendations: All 8 features
were identified as contributory, and no feature was recommended for exclusion. A non-linear term was
recommended for the _age_ feature. The framework has identified 14 potential interactions: _age_- _tsize,_ _age-estrec, estrec-pnodes_, _progrec-age, progrec-pnodes, progrec-estrec, progrec-horTh, progrec-_ _tgrade, progrec-menostat, horTh-menostat, horTh-tsize, horTh-tgrade, horTh-pnodes,_ and _horTh-age._

A refined Cox model incorporating all recommendations achieved a C-index of 0.687 (95% CI 0.687-
0.687), which greatly improved the discrimination over the baseline model. The refined model remained
well-calibrated (slope: 0.945; intercept: 0.112) (Figure 6; B)

**ACT.** The baseline Cox model achieved the C-index of 0.725 (95% CI 0.725-0.725) on the test set,
with a calibration slope of 1.156 and intercept -0.196. The exploratory RSF model achieved C-index of
0.733 (95% CI 0.733-0.733) with a calibration slope of 1.628 and intercept -0.631 (Figure 7; B).

Figure 7; A demonstrated the FA analysis results for the ACT data. Based on the FA analysis, the
workflow recommended excluding the feature _hemophil_ and suggested including non-linear terms for
_karnof_ and _age_. It also identified 11 potential interactions: _ivdrug_- _karnof, cd4-karnof, cd4-raceth_,
_priorzdv_- _ivdrug_, _raceth_- _ivdrug_, _raceth_- _priorzdv_, _raceth_- _sex_, _age_- _strat2_, _age_- _priorzdv_, _age_- _karnof_, _age_-
_raceth_.

After integrating all recommendations, the refined Cox model achieved a C-index of 0.770 (95% CI
0.770-0.770) with the calibration slope of 1.650 and intercept -0.656 (Figure 7; B). The discriminative
performance greatly improved over the baseline model, with the calibration performance remaining
similar.

These findings demonstrate that our proposed Recommender can consistently generate clinically
relevant hypotheses for study design across different data sets and clinical questions.

## Discussion

In this study, we developed and evaluated an Exploratory AI Recommender designed to support
predictive study design in high-dimensional clinical datasets. Rather than using AI as an opaque final
predication model, the framework uses a flexible explainable-AI module as an exploratory engine to
identify data-driven modelling insights that can then be translated into transparent statistical models. In
a fall risk case study, the system identified 22 potentially redundant predictors among 58 candidate
features, detected two non-linear associations, and uncovered 221 clinically plausible interactions from
4,950 possible feature pairs. An augmented Cox Proportional Hazards model incorporating these
findings significantly exceeded the baseline in both discrimination and calibration. By deploying AI
strictly as an exploratory mechanism rather than a direct predictor, our framework can help researchers
navigate complex feature spaces while preserving the auditability and mathematical transparency
required in regulated clinical environments. This explicit separation of automated discovery from final
clinical prediction resolves the tension between algorithmic accuracy and interpretability.

The Recommender’s outputs align with established literature, confirming frailty and age as dominant

such as age with polypharmacy and comorbidities³³ , as well as specific drug-comorbidity, drug-drug
and demographics-drug interactions (e.g., dementia with antipsychotic drugs 34–36 , non-steroidal antiinflammatory drugs (NSAIDs) with opioid analgesics 37,38 , and frailty with antihistamines 39,40 ). Beyond confirming existing knowledge, our framework also identified some novel hypotheses that deserve
further exploration. For example, the system identified a non-linear relationship between alcohol status
41
and FRI risk (supported by recent literature) and a compounded risk interaction between dementia
and antispasmodic medications (can be explained as the anticholinergic effects carried by
antispasmodics can result in impairment of memory function⁴², mirroring the symptoms of dementia).
Crucially, the Recommender supports rather than replaces clinical judgment. For instance, while the
tool suggested excluding visual impairment, likely due to low frequency/predictive power, the
framework’s transparent design allows researchers to critically evaluate such data-driven
recommendations.

This work extends previous research to predictive model designs in several ways. First, the framework
is not simply a feature selection tool. Existing approaches, including robust variable selection and
43
regularization-based methods for Cox models, provide rigorous strategies for deriving effective
predictor sets, improving model stability, and reducing overfitting within prespecified modelling
frameworks. However, these methods are primarily designed to determine which variables should be
retained in a final model. In contrast, our framework combines a flexible non-linear exploratory model
with explainable AI to generate broader design-relevant insights, including candidate feature
exclusions, potential non-linear effects, interaction structures, and subgroup-specific predictor
behaviour. These outputs are intended not only to support model development, but also to help
researchers understand why a feature may be informative, how its contribution may vary across patient
subgroups, and which feature relationships may warrant formal statistical evaluation. In this sense, the
framework complements rather than replaces established biostatistical methods by prioritizing
clinically and statistically plausible signals from a large candidate space for targeted follow-up using
conventional tools, including penalized Cox models, restricted cubic splines, interaction terms, and
likelihood ratio tests.

Second, the Recommender provides a mechanism for exploring subgroup-specific predictor behaviour
that may be overlooked by conventional model development. Traditional models often emphasize highrisk populations, yet patients classified as low risk are not necessarily free from risk; rather, potential
44
risk factors may be compensated by other protective factors. Our extreme-group analysis revealed that
NSAIDs, although contributing minimally in the high-risk cohort, was a significant predictor
specifically in low-risk cohorts. Identifying these predictors in low-risk groups offers new opportunities
for early, targeted preventive interventions. Furthermore, this stratified mechanism offers visibility into
how clinical features behave differently across distinct subpopulations: atrial fibrillation generally
decreased predicted risk for patients under 65 years but increased it among those aged 65 years or older
(Figure 5). While the framework does not automatically calculate formal mathematical fairness metrics,
its architecture actively facilitates algorithmic equity audits. Researchers can define strata using
protected characteristics such as sex, ethnicity, or socioeconomic deprivation. The system then
systematically isolates and compares variable importance across these demographic subsets. By
exposing these subgroup-specific deviations, the framework provides the exact insights required to
identify bias early in the study design.

remarkable predictive capabilities with complex and large-scale biomedical data, 45 but their opacity

conventional statistical models, we address the accuracy-interpretability trade-off without the fidelity
issues of post-hoc explainable AI. 47 The exploratory RSF achieving a higher C-index than the advantage in highly regulated clinical environments where a fixed, transparent formula is often
preferred over an ensemble of trees for safety and auditability.

Furthermore, our framework demonstrates some utility in a “hard-to-improve” scenario as the
improvement in C-index (0.010) is statistically significant but numerically modest. Relatively simple
models can perform reasonably well on high-quality, large-scale datasets, leading to great difficulty in
achieving marginal gains. However, in large-scale population health, even marginal gains in
discrimination and calibration can lead to significantly better resource allocation and risk stratification
when applied to hundreds of thousands of patients. Our approach is: scalable as it rapidly explores
thousands of pairwise interactions; efficient as it avoids the computational demands of complex
48,49
architectures like Graph Neural Networks; adaptable as it is applicable to different models (e.g.,
DeepSurv⁵⁰ or diagnosis prediction) and clinical datasets. While SHAP is utilized here due to its
theoretical foundations in game theory, the framework is attribution-agnostic. Researchers may
52
consider other techniques like Integrated Gradients⁵¹ or SurvSHAP(t) for time-dependent explanations,
depending on the computational budget and the specific exploratory model used.

This framework offers practical implications for clinical research. It streamlines future data collection
by reducing variable burden without sacrificing predictive performance, can guide feature selection in
53
further causal studies, and enables researchers to move beyond preconceived hypotheses. More
broadly, the framework encourages researchers to move beyond purely literature-driven or knowledgebased model specification by providing a systematic, data-driven mechanism for discovering important
features, non-linearities, interactions, and subgroup-specific effects. These insights may also inform
subsequent causal studies, although they should not be interpreted as causal evidence without further
causal design and validation.

This study has several limitations. First, our interaction terms were restricted to (already challenging)
first-order pairs to ensure computational feasibility. Higher-order interactions were not explored, but
54
are a potential focus for future research, where computational complexity is the main concern. Second,
the validity of the recommendations depends on the exploratory model's performance (e.g., RSF).
Suboptimal discrimination or calibration could introduce bias into FAs, necessitating careful model
selection or ensemble approaches. Thus, we advise using the recommendations produced only with high
performing exploratory models (high C-index and stable calibration), and leave investigation into
quality metrics of FAs to future work. Third, our analysis focused on large-scale populations rather than
individual longitudinal trajectories, leaving temporal dependencies out of scope, though in principle
52
applicable with extensions. Fourth, we applied recommendations in a fixed sequence, starting with
feature exclusion to reduce complexity, which may yield different results than alternative ordering.
Fifth, the baseline Cox model was intentionally kept ‘naïve’ to represent standard literature-driven
practice. We acknowledge that penalized models like LASSO or Elastic Net⁵⁵ are strong benchmarks.
While our current study focuses on the discovery of interactions and non-linearities via explainable AI,
future work should benchmark this framework against these established regularization techniques to
quantify the gain of explainable AI-driven design. Finally, we emphasize that FAs represent predictive
associations, not causal relationships; they denote contributions to the model's output rather than the
clinical outcome itself. Any clinical interventions based on these findings would require subsequent
causal discovery or randomized controlled trials.

## Conclusion

We demonstrated that explainable AI can uncover complex feature relationships within highdimensional clinical datasets. This data-driven exploratory approach showed the potential to improve
the robustness of predictive cohort study design by augmenting traditional, expert-led methods. These findings also suggest that explainable AI-informed insights can generate novel hypotheses that may
warrant further investigation.

## Data Availability

The data that support the findings of this study are available from DataLoch ([https://dataloch.org/](https://dataloch.org/)), but
restrictions apply to the availability of these data, which were used under license for the current study,
and so are not publicly available. DataLoch data are available to researchers who complete governance
training and obtain approvals. Access to DataLoch requires submission of a proposal, with investigator
support and approval as needed. DataLoch data is stored in an NHS safe haven and can be accessed
remotely. GBSG2 and ACT are publicly available.

## Code Availability

The code to replicate the analysis on publicly available datasets (GBSG2 and ACT) is available on
GitHub via [https://github.com/CHAI-UK/XAI-insight-discovery/](https://github.com/CHAI-UK/XAI-insight-discovery/).

## References

1. Khan SS, Matsushita K, Sang Y, et al. Development and Validation of the American Heart
   Association’s PREVENT Equations. _Circulation_. 2024;149(6):430-449.
   doi:10.1161/CIRCULATIONAHA.123.067626
2. Hippisley-Cox J, Coupland C, Brindle P. Development and validation of QRISK3 risk prediction
   algorithms to estimate future risk of cardiovascular disease: prospective cohort study. _BMJ_.
   2017;357. doi:10.1136/BMJ.J2099
3. Artetxe A, Beristain A, Graña M. Predictive models for hospital readmission risk: A systematic
   review of methods. _Comput Methods Programs Biomed_. 2018;164:49-64.
   doi:10.1016/j.cmpb.2018.06.006
4. Shipe ME, Deppen SA, Farjah F, Grogan EL. Developing prediction models for clinical use using
   logistic regression: an overview. _J Thorac Dis_. 2019;11(Suppl 4):S574.
   doi:10.21037/JTD.2019.01.25
5. Matsuo K, Purushotham S, Jiang B, et al. Survival outcome prediction in cervical cancer: Cox
   models vs deep-learning model. _Am J Obstet Gynecol_. 2019;220(4):381.e1-381.e14.
   doi:10.1016/J.AJOG.2018.12.030
6. Esteva A, Robicquet A, Ramsundar B, et al. A guide to deep learning in healthcare. _Nature_ _Medicine 2019 25:1_. 2019;25(1):24-29. doi:10.1038/s41591-018-0316-z
7. Miotto R, Wang F, Wang S, Jiang X, Dudley JT. Deep learning for healthcare: review,
   opportunities and challenges. _Brief Bioinform_. 2018;19(6):1236-1246.
   doi:10.1093/BIB/BBX044
8. Carabantes M. Black-box artificial intelligence: an epistemological and critical analysis. _AI &_ _SOCIETY 2019 35:2_. 2019;35(2):309-317. doi:10.1007/S00146-019-00888-W
9. van Royen FS, Weerts HJP, de Hond AAH, et al. In humble defense of unexplainable black box
   prediction models in healthcare. _J Clin Epidemiol_. 2026;189.
   doi:10.1016/j.jclinepi.2025.112013

* * *

10. Carriero A, de Hond A, Cappers B, et al. Explainable AI in healthcare: to explain, to predict, or
    to describe? _Diagn Progn Res_. 2025;9(1). doi:10.1186/S41512-025-00213-8
11. Hassan M, Kushniruk A, Borycki E. Barriers to and Facilitators of Artificial Intelligence
    Adoption in Health Care: Scoping Review. _JMIR Hum Factors_. 2024;11(1):e48633.
    doi:10.2196/48633
12. Varghese J. Artificial Intelligence in Medicine: Chances and Challenges for Wide Clinical
    Adoption. _Visc Med_. 2020;36(6):443-449. doi:10.1159/000511930
13. Mennella C, Maniscalco U, De Pietro G, Esposito M. Ethical and regulatory challenges of AI
    technologies in healthcare: A narrative review. _Heliyon_. 2024;10(4):e26297.
    doi:10.1016/j.heliyon.2024.e26297
14. Hassija V, Chamola V, Mahapatra A, et al. Interpreting Black-Box Models: A Review on
    Explainable Artificial Intelligence. _Cognitive Computation 2023 16:1_. 2023;16(1):45-74.
    doi:10.1007/S12559-023-10179-8
15. Winter E. Chapter 53 The shapley value. _Handbook of Game Theory with Economic_ _Applications_. 2002;3. doi:10.1016/S1574-0005(02)03016-3
16. Ortigossa ES, Gonçalves T, Nonato LG. EXplainable Artificial Intelligence (XAI)—From Theory
    to Methods and Applications. _IEEE Access_. 2024;12:80799-80846.
    doi:10.1109/ACCESS.2024.3409843
17. Mridha K, Ghimire S, Shin J, Aran A, Uddin MM, Mridha MF. Automated Stroke Prediction
    Using Machine Learning: An Explainable and Exploratory Study With a Web Application for
    Early Intervention. _IEEE Access_. 2023;11. doi:10.1109/ACCESS.2023.3278273
18. Ahmed ZU, Sun K, Shelly M, Mu L. Explainable artificial intelligence (XAI) for exploring spatial
    variability of lung and bronchus cancer (LBC) mortality rates in the contiguous USA. _Sci Rep_.
    2021;11(1). doi:10.1038/s41598-021-03198-8
19. Klauschen F, Dippel J, Keyl P, et al. Toward Explainable Artificial Intelligence for Precision
    Pathology. _Annual Review of Pathology: Mechanisms of Disease_. 2024;19.
    doi:10.1146/annurev-pathmechdis-051222-113147
20. Temkov S. Explainable AI for Discovering Disease Biomarkers: A Survey. In: Gül ÖM, Fiorini P,
    Kadry SN, eds. _7th EAI International Conference on Robotic Sensor Networks_. Springer Nature
    Switzerland; 2024:185-192.
21. Yagin FH, Aygun U, Algarni A, Colak C, Al-Hashem F, Ardigò LP. Platelet Metabolites as
    Candidate Biomarkers in Sepsis Diagnosis and Management Using the Proposed Explainable
    Artificial Intelligence Approach. _J Clin Med_. 2024;13(17). doi:10.3390/jcm13175002
22. Burugadda VR, Dutt V, Mamta, Vyas N. Personalized Cardiovascular Disease Risk Prediction
    Using Random Forest: An Optimized Approach. In: _Proceedings - 2023 IEEE World Conference_ _on Applied Intelligence and Computing, AIC 2023_. 2023\.
    doi:10.1109/AIC57670.2023.10263915
23. Khani M, Luo J, Assadi Shalmani M, Taleban A, Adams J, Friedland DR. Advancing personalized
    healthcare: leveraging explainable AI for BPPV risk assessment. _Health Inf Sci Syst_.
    2024;13(1):1. doi:10.1007/s13755-024-00317-3

* * *

24. Gosiewska A, Kozak A, Biecek P. Simpler is better: Lifting interpretability-performance tradeoff via automated feature engineering. _Decis Support Syst_. 2021;150:113556.
    doi:10.1016/J.DSS.2021.113556
25. Liu X, Morelli D, Littlejohns TJ, Clifton DA, Clifton L. Combining machine learning with Cox
    models to identify predictors for incident post-menopausal breast cancer in the UK Biobank.
    _Scientific Reports 2023 13:1_. 2023;13(1):9221-. doi:10.1038/s41598-023-36214-0
26. Blayney MC, Reed MJ, Masterson JA, et al. Multimorbidity and adverse outcomes following
    emergency department attendance: population based cohort study. _BMJ Medicine_.
    2024;3(1):e000731. doi:10.1136/bmjmed-2023-000731
27. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for
    reporting clinical prediction models that use regression or machine learning methods. _BMJ_.
    2024;385. doi:10.1136/BMJ-2023-078378
28. Lansbury LN, Roberts HC, Clift E, Herklots A, Robinson N, Sayer AA. Use of the electronic
    Frailty Index to identify vulnerable patients: A pilot study in primary care. _British Journal of_ _General Practice_. 2017;67(664). doi:10.3399/bjgp17X693089
29. Ishwaran H, Kogalur UB, Blackstone EH, Lauer MS. Random survival forests. _Annals of Applied_ _Statistics_. 2008;2(3). doi:10.1214/08-AOAS169
30. Sauerbrei W, Bastert G, Bojar H, et al. Randomized 2 x 2 trial evaluating hormonal treatment
    and the duration of chemotherapy in node-positive breast cancer patients: An update based
    on 10 years’ follow-up. _Journal of Clinical Oncology_. 2000;18(1). doi:10.1200/jco.2000.18.1.94
31. Hosmer DW, Lemeshow S, May S. _Applied Survival Analysis: Regression Modeling of Time to_ _Event Data: Second Edition_. 2011\. doi:10.1002/9780470258019
32. Yang ZC, Lin H, Jiang GH, et al. Frailty Is a Risk Factor for Falls in the Older Adults: A
    Systematic Review and Meta-Analysis. _Journal of Nutrition, Health and Aging_. _Springer-Verlag_
    \*Italia s.r.l.\*2023;27(6):487-495. doi:10.1007/s12603-023-1935-8
33. Prescribing in the elderly \| Medicines guidance \| BNF \| NICE. Accessed October 14, 2025.
    [https://bnf.nice.org.uk/medicines-guidance/prescribing-in-the-elderly/](https://bnf.nice.org.uk/medicines-guidance/prescribing-in-the-elderly/)
34. Mok PLH, Carr MJ, Guthrie B, et al. Multiple adverse outcomes associated with antipsychotic
    use in people with dementia: population based matched cohort study. _BMJ_. Published online
35. doi:10.1136/bmj-2023-076268
36. Korkatti-Puoskari N, Tiihonen M, Caballero-Mora MA, Topinkova E, Szczerbińska K,
    Hartikainen S. Therapeutic dilemma’s: antipsychotics use for neuropsychiatric symptoms of
    dementia, delirium and insomnia and risk of falling in older adults, a clinical review. _Eur_ _Geriatr Med_. _Springer Science and Business Media Deutschland GmbH_. 2023;14(4):709-720.
    doi:10.1007/s41999-023-00837-3
37. D’Alton M, Eustace A. Antipsychotic Prescribing and Falls Risk in Nursing Home Residents with
    Dementia. _Age Ageing_. 2024;53(Supplement\_4):afae178.216.
    doi:10.1093/ageing/afae178.216
38. Khan NF, Bykov K, Katz JN, Glynn RJ, Vine SM, Kim SC. Risk of fall or fracture with concomitant
    use of prescription opioids and other medications in osteoarthritis patients.
    _Pharmacoepidemiol Drug Saf_. 2024;33(3). doi:10.1002/pds.5773

* * *

38. Herzig SJ, Anderson TS, Jung Y, Ngo L, Kim DH, McCarthy EP. Relative risks of adverse events
    among older adults receiving opioids versus NSAIDs after hospital discharge: A nationwide
    cohort study. _PLoS Med_. 2021;18(9). doi:10.1371/journal.pmed.1003804
39. Cho H, Myung J, Suh HS, Kang HY. Antihistamine use and the risk of injurious falls or fracture
    in elderly patients: a systematic review and meta-analysis. _Osteoporosis International_.
    _Springer London_. 2018;29(10):2163-2170. doi:10.1007/s00198-018-4564-z
40. Naharci MI, Tasci I. Frailty status and increased risk for falls: The role of anticholinergic
    burden. _Arch Gerontol Geriatr_. 2020;90. doi:10.1016/j.archger.2020.104136
41. Sun Y, Zhang B, Yao Q, et al. Association between usual alcohol consumption and risk of falls
    in middle-aged and older Chinese adults. _BMC Geriatr_. 2022;22(1):1-11. doi:10.1186/S12877-
    022-03429-1/FIGURES/2
42. Ruxton K, Woodman RJ, Mangoni AA. Drugs with anticholinergic effects and cognitive
    impairment, falls and all-cause mortality in older adults: A systematic review and metaanalysis. _Br J Clin Pharmacol_. 2015;80(2):209-220. doi:10.1111/bcp.12617
43. Zhang Y, Muller S. Robust variable selection methods with Cox model-a selective practical
    benchmark study. _Brief Bioinform_. 2024;25(6). doi:10.1093/BIB/BBAE508
44. Montero-Odasso M, Pieruccini-Faria F, Son S, et al. Fall risk stratification in older adults: low
    and not-at-risk status still associated with falls and injuries. _Age Ageing_. 2025;54(3).
    doi:10.1093/AGEING/AFAF064
45. Huang Y, Li J, Li M, Aparasu RR. Application of machine learning in predicting survival
    outcomes involving real-world data: a scoping review. _BMC Med Res Methodol_. 2023;23(1).
    doi:10.1186/s12874-023-02078-1
46. Bektaş AB, Gönen M. Machine Learning for Medicine Must Be Interpretable, Shareable,
    Reproducible and Accountable by Design. Published online August 22, 2025.
    [http://arxiv.org/abs/2508.16097](http://arxiv.org/abs/2508.16097)
47. Rudin C. Stop explaining black box machine learning models for high stakes decisions and use
    interpretable models instead. _Nat Mach Intell_. _Nature Research_. 2019;1(5):206-215.
    doi:10.1038/s42256-019-0048-x
48. Kwak H, Lee M, Yoon S, Chang J, Park S, Jung K. Drug-Disease Graph: Predicting Adverse Drug
    Reaction Signals via Graph Neural Network with Clinical Data. In: _Lecture Notes in Computer_ _Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in_ _Bioinformatics)_. 12085 LNAI. Springer; 2020:633-644. doi:10.1007/978-3-030-47436-2\_48
49. Al-Rabeah MH, Lakizadeh A. Prediction of drug-drug interaction events using graph neural
    networks based feature extraction. _Sci Rep_. 2022;12(1). doi:10.1038/s41598-022-19999-4
50. Katzman JL, Shaham U, Cloninger A, Bates J, Jiang T, Kluger Y. DeepSurv: Personalized
    treatment recommender system using a Cox proportional hazards deep neural network. _BMC_ _Med Res Methodol_. 2018;18(1). doi:10.1186/s12874-018-0482-1
51. Sundararajan M, Taly A, Yan Q. Axiomatic attribution for deep networks. _34th International_ _Conference on Machine Learning, ICML 2017_. 2017;7:5109-5118.

* * *

52. Krzyziński M, Spytek M, Baniecki H, Biecek P. SurvSHAP(t): Time-dependent explanations of
    machine learning survival models. _Knowl Based Syst_. 2023;262:110234.
    doi:10.1016/J.KNOSYS.2022.110234
53. Kuzma JW. _Basic Statistics for the Health Sciences_. Vol 4. 1992.
54. Butler K, Feng G, Djurić PM. Higher-Order Feature Attribution: Bridging Statistics, Explainable
    AI, and Topological Signal Processing. _ICASSP 2026 - 2026 IEEE International Conference on_ _Acoustics, Speech and Signal Processing (ICASSP)_. Published online May 3, 2026:5261-5265.
    doi:10.1109/ICASSP55912.2026.11461829
55. Zou H, Hastie T. Regularization and Variable Selection Via the Elastic Net. _J R Stat Soc Series B_ _Stat Methodol_. 2005;67(2):301-320. doi:10.1111/J.1467-9868.2005.00503.X
56. McCartney G, Hoggett R. How well does the Scottish Index of Multiple Deprivation identify
    income and employment deprived individuals across the urban-rural spectrum and between
    local authorities? _Public Health_. 2023;217:26-32. doi:10.1016/J.PUHE.2023.01.009
57. Sikron FH, Schenker R, Koom Y, et al. Development and validation of an electronic frailty
    index in a national health maintenance organization. _Aging_. 2024;16(20):13025-13038.
    doi:10.18632/AGING.206141
58. Kuan V, Denaxas S, Gonzalez-Izquierdo A, et al. A chronological map of 308 physical and
    mental health conditions from 4 million individuals in the English National Health Service.
    _Lancet Digit Health_. 2019;1(2):e63-e77. doi:10.1016/S2589-7500(19)30012-3
59. de Vries M, Seppala LJ, Daams JG, et al. Fall-Risk-Increasing Drugs: A Systematic Review and
    Meta-Analysis: I. Cardiovascular Drugs. _J Am Med Dir Assoc_. 2018;19(4).
    doi:10.1016/j.jamda.2017.12.013
60. Seppala LJ, Wermelink AMAT, de Vries M, et al. Fall-Risk-Increasing Drugs: A Systematic
    Review and Meta-Analysis: II. Psychotropics. _J Am Med Dir Assoc_. 2018;19(4).
    doi:10.1016/j.jamda.2017.12.098
61. Seppala LJ, van de Glind EMM, Daams JG, et al. Fall-Risk-Increasing Drugs: A Systematic
    Review and Meta-analysis: III. Others. _J Am Med Dir Assoc_. 2018;19(4).
    doi:10.1016/j.jamda.2017.12.099
62. Sundararajan M, Najmi A. The many shapley values for model explanation. _37th International_ _Conference on Machine Learning, ICML 2020_. 2020;PartF168147-12.
63. Messalas A, Kanellopoulos Y, Makris C. Model-Agnostic Interpretability with Shapley Values.
    _10th International Conference on Information, Intelligence, Systems and Applications, IISA_ _2019_. Published online 2019. doi:10.1109/IISA.2019.8900669
64. Lundberg SM, Lee SI. A unified approach to interpreting model predictions. _Adv Neural Inf_ _Process Syst_. 2017;2017-December.
65. Lundstrom DD, Huang T, Razaviyayn M. A rigorous study of integrated gradients method and
    extensions to internal neuron attributions. In: _International Conference on Machine Learning_.
    2022:14485-14508.

* * *

66. Ribeiro MT, Singh S, Guestrin C. “Why should i trust you?” Explaining the predictions of any
    classifier. In: _Proceedings of the ACM SIGKDD International Conference on Knowledge_ _Discovery and Data Mining_. Vols 13-17-August-2016. 2016. doi:10.1145/2939672.2939778

## Acknowledgements

We acknowledge the support of the UKRI AI programme, and the Engineering and Physical Sciences
Research Council (EPSRC), for the Causality in Healthcare AI Hub \[grant number EP/Y028856/1\].
Junyu Yan is supported in part by the Advanced Care Research Center by the Ph.D. studentship.

* * *

**Figure 1**. Overview of the incorporated methodology.
\[Image: Image82\]

The incorporated methodology consists of three main steps. _Step 1_ intends to mimic the usual knowledge-driven
practice without any AI-based tools\*.\* The raw _Data_ is curated by the research team in accordance with their
_Research Question_ and using their _Domain Knowledge_. The resulting _Curated Data_ is then used with a naive Cox
model to obtain the _Baseline Performance. Step 2_ demonstrates the use of our proposed _Exploratory AI_ _Recommender_, a data-driven framework to obtain feature-related recommendations. _Curated Data_, prepared in
the previous step, is fed into the _Exploratory Model (Step 2a)_ that uses flexible AI methods (e.g., _Random Survival_ _Forest_) to capture complex data patterns. _Model Interpretation_ techniques ( _Step 2b_), such as _Feature Attributions_,
are then applied to extract those patterns from the _Exploratory Model_. Next, _Feature Attributions_ are processed
with a pre-defined set of rules (see Figure 2) to obtain feature-related _Recommendations_ ( _Step 2c_). In _Step 3_, we
evaluate the effectiveness of the provided recommendations. To achieve this, we take the _Baseline Model_ from
_Step 1_ and extend it with recommendations from _Step 2c_. The performances of augmented models are then
compared to the performance of the baseline model using _C-index_ and _Calibration_ plots.

* * *

**Figure 2.** Step 2c of our proposed methodology providing feature-related recommendations.

\[Image: Image91\]
There are five patterns of feature attribution values to be recognized (A-E), based on which our framework makes
three types of _Recommendations_. Three of the patterns (A-C) are associated with stratification and involve
observing groups of points that can be separated based on: A) feature attribution sign, B) feature values, and C)
feature attribution values. Pattern A) fits when positive and negative feature attributions form distinct groups.
Pattern B) can be recognized when separate groups consist of different feature values. Pattern C) may involve
mixed feature values, but the distinct groups are identified based on separation across feature attribution values.
Once the groups are identified, feature attributions are created for each stratum, which notably includes finding a
new reference point for each group (feature-average within each stratum). The values for both strata are analyzed
for differences in other (not stratified on) features (y and z in the figure). If a feature’s distributions are statistically
different between the two strata (e.g., feature y) then our framework recommends including an interaction between
that feature (y) and the feature we stratified on (x). The other two patterns (D-E) do not involve stratification. If
feature attributions (x-axis) and feature values (colors) are mixed but not centered around and not close to zero
(pattern D), it suggests the feature influences the model in a non-linear way, which is why our framework
recommends creating a non-linear term (e.g., quadratic) for that feature moving forward. The fifth and last pattern
involves detecting feature attributions that are mostly centered around the value of zero (pattern E). If this is the
case, it suggests that the feature has negligible or no impact on model predictions, leading to recommended
exclusion of the feature from further analysis.

* * *

**Figure 3.** Evaluation of the recommendations provided by the proposed framework as compared to the naïve baseline model.
\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

\[Image: Image94\]

* * *

**Figure 4.** Feature attributions from Random Survival Forest estimating FRI risks among individuals within low-risk and high-risk cohorts.
\[Image: Image97\]

Feature attributions for low-risk and high-risk groups. Each dot corresponds to a single patient observation, and its position along x-axis indicates its influence on the risk of an
FRI event. Positive FAs (right of 0) indicate that a feature increased the FRI risk, whereas negative FAs (left of 0) indicate that a feature is correlated with decreased FRI risk.
Color is used to indicate the value of included feature characteristics. Red and blue indicate higher and lower feature values, respectively. Medications and comorbidities are
binary features hence red indicates presence of the listed characteristic (e.g., diagnosis of _angina_) and blue its absence (e.g., no diagnosis of _angina_). Marked data points
(dashed lines) showcase examples of how the pre-defined patterns (see Figure 2) are being processed into recommendations in practice.

* * *

**Figure 5.** Age-stratified feature attribution summary among low-risk individuals with age lower and greater than 65.
\[Image: Image100\]

\[Image: Image100\]
Feature attributions for two age groups. Patients were stratified into lower-age group (n=1023) and higher-age group (n=536). The low-age group included individuals whose
predicted risk score was within a predefined score margin based on an average low-risk patient with age below 65 in the test data (feature averaged across all patients in the
test data with no records of falls and age below 65). This margin was defined as a Euclidean distance less than 0.01 multiplied by the standard deviation of the model’s predictions
across the test set. The high-age cohort included individuals whose predicted risk score was within the same score margin but whose age is above 65. Marked data points
(dashed lines) show examples of patterns that lead to recommended interactions. Specifically, marked points show different distributions in the two age strata, which is a sign of
potential interactions with the _age_ feature

* * *

**Figure 6.** Results for the GBSG2 dataset.

A (top): Feature attributions obtained on the low-risk (left) and high-risk (right) populations. B (bottom): Calibration plots and predictive performances (C-index) of the
baseline Cox PH model, the RSF exploratory model, and the Cox PH model augmented with all recommendations.

* * *

**Figure 7.** Results for the ACT dataset.

A (top): Feature attributions obtained on the low-risk (left) and high-risk (right) populations. B (bottom): Calibration plots and predictive performances (C-index) of the
baseline Cox PH model, the RSF exploratory model, and the Cox PH model augmented with all recommendations.

* * *

## Supplementary Information

**Supplementary Table 1: International Classification of Diseases Clinical Codes** **for Fall and Related Injuries**. **Falls were identified based on 72 Read version 2** **(Read2) codes (ascertaining falls in GP records), 89 ICD-10 codes (ascertaining** **falls in hospital discharge diagnoses), and three presenting complaint codes** **(ascertaining falls in emergency department \[ED\] data). Relevant fractures** **were identified using 78 GP Read2 codes, seven ICD-10 codes and seven ED** **diagnosis discharge codes**
Code

| Type of FRI | Code Type | Diagnosis Codes |  |
| --- | --- | --- | --- |
| Falls | Read Codes | 16D..00, 16D6.00, 8BIG.00, R200.12, TC...00, TC0..00,TC00.00,TC00000,TC01.00,TC01000,TC01200,TC02.00,TC02000,TC02100,TC02z00,T04..00,TC0z.00,TC...11,TC42.00,TC42000,TC42z00,TC5.00,TC50.00,TC51.00,U10..00,U101400,U101z00,U107.00,U107z00,U108000,U10A.00,U10A511,U10Az00,U10J.00,U10J000,U10z000,U10z00,U10zz00,U10z400,T240100,TCy..00,TCy0.00,U105000,U105.00,U107000,TCz..00,TCz.00,T040100,U101100,TC50.00,U10z.00,T040.00,TC42100,Tcyz.00,TC52.00,TC7..00,EMINSNQPA3,TC5..99,^ESCTEL585171,HNGNQRF118,U101.00,TC5z.00,U108z00,U101000,^ESCTUN670525,16D1.00,TC0..99,TC52.00,TCz..99,U10A000 |  |
| Fracture | ICD-10 | W01X,W010,W011,W012,W013,W014,W015,W016,W017,W018,W019,W05X,W050,W051,W052,W053,W054,W055,W056,W057,W058,W059,W06X,W060,W061,W062,W063,W064,W065,W066,W067,W068,W069,W70X,W070,W071,W072,W073,W074,W075,W076,W077,W078,W079,W08X,W080,W081,W082,W083,W084,W085,W086,W087,W088,W089,W10X,W100,W101,W102,W103,W104,W105,W106,W107,W108,W109,W18X,W180,W181,W182,W183,W184,W185,W186,W187,W188,W189,W19X,W190,W191,W192,W193,W194,W195,W196,W197,W198,W199,R296 |  |
| Fracture | Presenting complaint | Fall, unsteady on feet, unsteady on feet/falls/longlie |  |
| Fracture | Read Codes | S300y11,S300z00,S302.00,S302000,S302100,S302200,S302300,S302400,S302z00,S304.00,S305.00,S30y.00,S30y.11,S30..00,S30..11,S300.00,S300000,S300100,S300200,S300300,S300311,S300400,S300500,S300600,S300700,S300800,S300900,S31z.00,7K1LM00,S234.00,S234.11,S234000,S234100,S234111,S234200,S234600,S234700,S234800,S234900,S234911,S234912,S234A00,S234A11,S234A12,S234C00,S234D00,S234E00,S234F00,S234G00,S234z00,S23B.00,S23C.00,S23x000,S23x100,S23x111,S4C0000,C40100,C42000,C42100,S234400,S4C2.00,S234500,S4C0.00,7K1LF00,S22..00,S220.00,S220000,S220100,S220200,S220400,S220500,S220600,S220700,S220z00,S222000,S226.00,S222.00 |  |

* * *

| Type of FRI | Code Type | Diagnosis Codes |
| --- | --- | --- |
|  | ICD-10 | S42.2,S52.5,S52.6,S62.1,S72.0,S72.1,S72.2 |
|  | Diagnosis Discharge | BBS520.2,BBS522,BBS523.1,BBS523.2,BBS524,BBS720,BBS423 |
|  |  |  |

* * *

**Supplementary Table 2: List of 27 high-level long-term conditions summarised** **from HDRUK CALIBER phenotypes combining primary care and hospital** **records. The number of phenotypes combined for each long-term condition is** **shown.**

| Condition | Number of CALIBER phenotypes combined |
| --- | --- |
| Angina | 12 |
| Anxiety disorder | 2 |
| Asthma | 2 |
| Atrial fibrillation | 8 |
| Cancers | 66 |
| Coronary | 3 |
| Dementia | 2 |
| Depression | 2 |
| Diabetes mellitus | 6 |
| End stage renal disease | 2 |
| Epilepsy | 2 |
| Gout | 2 |
| Heart failure | 2 |
| Hypertension | 3 |
| Hyperthyroidism | 2 |
| Multiple sclerosis | 1 |
| Multiple valve dz | 1 |
| Myocardial infarction | 7 |
| Osteoporosis | 2 |
| Parkinson's disease | 2 |
| Peripheral arterial disease | 5 |
| Pulmonary circulation disorders | 5 |
| Rheumatoid arthritis | 2 |
| Schizophrenia, schizotypal and delusional disorders | 2 |
| Stroke | 6 |
| Transient ischaemic attack | 2 |
| Visual impairment and blindness | 2 |

* * *

**Supplementary Table 3: Detailed list of HDRUK CALIBER phenotypes that are combined into the 27 high-level LTC groups listed into** **Table S2. Each CALIBER phenotype and subcategory may be mapped to multiple GP (Read) or Hospital (ICD-10) codes as per published** **codelists on the HDRUK Phenotype Library.**

| High-Level LTC Group | CALIBER Phenotype Name | CALIBER Phenotype Subcategory |
| --- | --- | --- |
| Angina | Stable angina | CABG Performed(2) |
| Angina | Stable angina | Chest pain, attributed to coronary causes(4) |
| Angina | Stable angina | History of stable angina(1) |
| Angina | Stable angina | PCI performed(2) |
| Angina | Stable angina | Results abnormal(3) |
| Angina | Stable angina | Results abnormal-indicative of ischaemia(T-wave changes or ST-depression)(2) |
| Angina | Stable angina | Stable angina(4) |
| Angina | Stable angina | Stable angina admission(4) |
| Angina | Unstable angina | ACS diagnosed(3) |
| Angina | Unstable angina | Unstable angina(3) |
| Angina | Unstable angina | Worsening angina(2) |
| Angina | Unstable angina | yes(1) |
| Anxiety disorders | Anxiety disorders | Diagnosis of Anxiety disorders |

* * *

| Anxiety disorders | Anxiety disorders | History of Anxiety disorders |
| --- | --- | --- |
| Asthma | Asthma | Diagnosis of Asthma |
| Asthma | Asthma | History of Asthma |
| Atrial Fibrillation | Atrial fibrillation | Atrial fibrillation monitoring(2) |
| Atrial Fibrillation | Atrial fibrillation | Atrial fibrillation or flutter(6) |
| Atrial Fibrillation | Atrial fibrillation | Atrial fibrillation, not otherwise specified(5) |
| Atrial Fibrillation | Atrial fibrillation | Atrial flutter(7) |
| Atrial Fibrillation | Atrial fibrillation | Fibrillation and flutter |
| Atrial Fibrillation | Atrial fibrillation | History of atrial fibrillation or flutter(1) |
| Atrial Fibrillation | Atrial fibrillation | Paroxysmal atrial fibrillation(3) |
| Atrial Fibrillation | Atrial fibrillation | Persistent or permanent atrial fibrillation(4) |
| Cancers | Hodgkin Lymphoma | Diagnosis of Hodgkin Lymphoma |
| Cancers | Hodgkin Lymphoma | History of Hodgkin Lymphoma |
| Cancers | Leukaemia | Diagnosis of Leukaemia |
| Cancers | Leukaemia | History of Leukaemia |
| Cancers | Monoclonal gammopathy of undetermined significance(MGUS) | 1 |
| Cancers | Monoclonal gammopathy of undetermined significance(MGUS) | Diagnosis of Monoclonal gammopathy of undetermined significance(MGUS) |

* * *

| Cancers | Multiple myeloma and malignant plasma cell neoplasms | Diagnosis of Multiple myeloma and malignant plasma cell neoplasms |
| --- | --- | --- |
| Cancers | Myelodysplastic syndromes | Diagnosis of Myelodysplastic syndromes |
| Cancers | Non-Hodgkin Lymphoma | Diagnosis of Non-Hodgkin Lymphoma |
| Cancers | Polycythaemia vera | Diagnosis of Polycythaemia vera |
| Cancers | Primary Malignancy\_biliary tract | Diagnosis of Primary Malignancy\_biliary tract |
| Cancers | Primary Malignancy\_Bladder | Diagnosis of Primary Malignancy\_Bladder |
| Cancers | Primary Malignancy\_Bladder | History of Primary Malignancy\_Bladder |
| Cancers | Primary Malignancy\_Bone and articular cartilage | Diagnosis of Primary Malignancy\_Bone and articular cartilage |
| Cancers | Primary Malignancy\_Bone and articular cartilage | History of Primary Malignancy\_Bone and articular cartilage |
| Cancers | Primary Malignancy\_Brain, Other CNS and Intracranial | Diagnosis of Primary Malignancy\_Brain, Other CNS and Intracranial |
| Cancers | Primary Malignancy\_Brain, Other CNS and Intracranial | History of Primary Malignancy\_Brain, Other CNS and Intracranial |
| Cancers | Primary Malignancy\_Breast | Diagnosis of Primary Malignancy\_Breast |
| Cancers | Primary Malignancy\_Breast | History of Primary Malignancy\_Breast |
| Cancers | Primary Malignancy\_Cervical | Diagnosis of Primary Malignancy\_Cervical |
| Cancers | Primary Malignancy\_Cervical | History of Primary Malignancy\_Cervical |
| Cancers | Primary Malignancy\_colorectal and anus | Diagnosis of Primary Malignancy\_colorectal and anus |
| Cancers | Primary Malignancy\_colorectal and anus | History of Primary Malignancy\_colorectal and anus |

* * *

| Cancers | Primary Malignancy\_Kidney and Ureter | Diagnosis of Primary Malignancy\_Kidney and Ureter |
| --- | --- | --- |
| Cancers | Primary Malignancy\_Kidney and Ureter | History of Primary Malignancy\_Kidney and Ureter |
| Cancers | Primary Malignancy\_Liver | Diagnosis of Primary Malignancy\_Liver |
| Cancers | Primary Malignancy\_Liver | History of Primary Malignancy\_Liver |
| Cancers | Primary Malignancy\_Lung and trachea | Diagnosis of Primary Malignancy\_Lung and trachea |
| Cancers | Primary Malignancy\_Lung and trachea | History of Primary Malignancy\_Lung and trachea |
| Cancers | Primary Malignancy\_Malignant Melanoma | Diagnosis of Primary Malignancy\_Malignant Melanoma |
| Cancers | Primary Malignancy\_Malignant Melanoma | History of Primary Malignancy\_Malignant Melanoma |
| Cancers | Primary Malignancy\_Mesothelioma | Diagnosis of Primary Malignancy\_Mesothelioma |
| Cancers | Primary Malignancy\_Mesothelioma | History of Primary Malignancy\_Mesothelioma |
| Cancers | Primary Malignancy\_Multiple independent sites | Diagnosis of Primary Malignancy\_Multiple independent sites |
| Cancers | Primary Malignancy\_Multiple independent sites | History of Primary Malignancy\_Multiple independent sites |
| Cancers | Primary Malignancy\_Oesophageal | Diagnosis of Primary Malignancy\_Oesophageal |
| Cancers | Primary Malignancy\_Oesophageal | History of Primary Malignancy\_Oesophageal |
| Cancers | Primary Malignancy\_Oro-pharyngeal | Diagnosis of Primary Malignancy\_Oro-pharyngeal |
| Cancers | Primary Malignancy\_Oro-pharyngeal | History of Primary Malignancy\_Oro-pharyngeal |
| Cancers | Primary Malignancy\_Other Organs | Diagnosis of Primary Malignancy\_Other Organs |
| Cancers | Primary Malignancy\_Other Organs | Possible Diagnosis of Primary Malignancy\_Other Organs |
| Cancers | Primary Malignancy\_Ovarian | Diagnosis of Primary Malignancy\_Ovarian |

* * *

| Cancers | Primary Malignancy\_Ovarian | History of Primary Malignancy\_Ovarian |
| --- | --- | --- |
| Cancers | Primary Malignancy\_Pancreatic | Diagnosis of Primary Malignancy\_Pancreatic |
| Cancers | Primary Malignancy\_Prostate | Diagnosis of Primary Malignancy\_Prostate |
| Cancers | Primary Malignancy\_Prostate | History of Primary Malignancy\_Prostate |
| Cancers | Primary Malignancy\_Stomach | Diagnosis of Primary Malignancy\_Stomach |
| Cancers | Primary Malignancy\_Stomach | History of Primary Malignancy\_Stomach |
| Cancers | Primary Malignancy\_Testicular | Diagnosis of Primary Malignancy\_Testicular |
| Cancers | Primary Malignancy\_Testicular | History of Primary Malignancy\_Testicular |
| Cancers | Primary Malignancy\_Thyroid | Diagnosis of Primary Malignancy\_Thyroid |
| Cancers | Primary Malignancy\_Thyroid | History of Primary Malignancy\_Thyroid |
| Cancers | Primary Malignancy\_Uterine | Diagnosis of Primary Malignancy\_Uterine |
| Cancers | Primary Malignancy\_Uterine | History of Primary Malignancy\_Uterine |
| Cancers | Secondary Malignancy\_Adrenal gland | Diagnosis of Secondary Malignancy\_Adrenal gland |
| Cancers | Secondary Malignancy\_Bone | Diagnosis of Secondary Malignancy\_Bone |
| Cancers | Secondary Malignancy\_Bowel | Diagnosis of Secondary Malignancy\_Bowel |
| Cancers | Secondary Malignancy\_Brain, Other CNS and Intracranial | Diagnosis of Secondary Malignancy\_Brain, Other CNS and Intracranial |

* * *

| Cancers | Secondary malignancy\_Liver and intrahepatic bile duct | Diagnosis of Secondary malignancy\_Liver and intrahepatic bile duct |
| --- | --- | --- |
| Cancers | Secondary Malignancy\_Lung | Diagnosis of Secondary Malignancy\_Lung |
| Cancers | Secondary Malignancy\_Lymph Nodes | Diagnosis of Secondary Malignancy\_Lymph Nodes |
| Cancers | Secondary Malignancy\_Other organs | Diagnosis of Secondary Malignancy\_Other organs |
| Cancers | Secondary Malignancy\_Other organs | Possible diagnosis of Secondary Malignancy\_Other organs |
| Cancers | Secondary Malignancy\_Pleura | Diagnosis of Secondary Malignancy\_Pleura |
| Cancers | Secondary Malignancy\_retroperitoneum and peritoneum | Diagnosis of Secondary Malignancy\_retroperitoneum and peritoneum |
| Coronary | Coronary heart disease not otherwise specified | Diagnosed |
| Coronary | Coronary heart disease not otherwise specified | Diagnosed(3) |
| Coronary | Coronary heart disease not otherwise specified | History of(1) |
| Dementia | Dementia | Diagnosis of Dementia |
| Dementia | Dementia | History of Dementia |
| Depression | Depression | Diagnosis of Depression |
| Depression | Depression | History of Depression |
| Diabetes Mellitus | Diabetes | Diabetes not otherwise specified(6) |
| Diabetes Mellitus | Diabetes | Insulin dependent diabetes(3) |
| Diabetes Mellitus | Diabetes | Non insulin dependent diabetes(4) |

* * *

| Diabetes Mellitus | Diabetes | Secondary diabetes(5) |
| --- | --- | --- |
| Diabetes Mellitus | Diabetes | Type I diabetes mellitus(3) |
| Diabetes Mellitus | Diabetes | Type II diabetes mellitus(4) |
| End Stage Renal Disease | End Stage Renal Disease | Diagnosis of End stage renal disease |
| End Stage Renal Disease | End Stage Renal Disease | Procedure for End stage renal disease |
| Epilepsy | Epilepsy | Diagnosis of Epilepsy |
| Epilepsy | Epilepsy | History of Epilepsy |
| Gout | Gout | Diagnosis of Gout |
| Gout | Gout | History of Gout |
| Heart Failure | Heart failure | Diagnosis of Heart failure |
| Heart Failure | Heart failure | History of Heart failure |
| Hypertension | Hypertension | History of hypertension(1) |
| Hypertension | Hypertension | Hypertension(3) |
| Hypertension | Hypertension | Secondary hypertension(4) |
| Hyperthyroidism | Hypo or hyperthyroidism | Diagnosis of Hypo or hyperthyroidism |
| Hyperthyroidism | Hypo or hyperthyroidism | History of Hypo or hyperthyroidism |
| Multiple Sclerosis | Liver fibrosis,sclerosis and cirrhosis | Diagnosis of Liver fibrosis,sclerosis and cirrhosis |
| Multiple Valve dz | Multiple valve dz | Diagnosis of Multiple valve dz |
| Myocardial Infarction | Myocardial infarction | Acute MI not further specified(5) |

* * *

| Myocardial Infarction | Myocardial infarction | Complications of MI(7) |
| --- | --- | --- |
| Myocardial Infarction | Myocardial infarction | History of MI(1) |
| Myocardial Infarction | Myocardial infarction | NSTEMI(4) |
| Myocardial Infarction | Myocardial infarction | Possible MI or uncertain date(2) |
| Myocardial Infarction | Myocardial infarction | STEMI(3) |
| Myocardial Infarction | Myocardial infarction | Subsequent MI(6) |
| Osteoporosis | Osteoporosis | Diagnosis of Osteoporosis |
| Osteoporosis | Osteoporosis | History of Osteoporosis |
| Parkinson's Disease | Parkinson's disease | Diagnosis of Parkinson's disease |
| Parkinson's Disease | Parkinson's disease | History of Parkinson's disease |
| Peripheral Arterial Disease | Peripheral arterial disease | history of PVD during a consultation |
| Peripheral Arterial Disease | Peripheral arterial disease | Leg or aortic embolism or thrombosis(8) |
| Peripheral Arterial Disease | Peripheral arterial disease | Other PAD procedures(3) |
| Peripheral Arterial Disease | Peripheral arterial disease | PAD procedure performed(3) |
| Peripheral Arterial Disease | Peripheral arterial disease | Peripheral vascular disease(7) |
| Pulmonary Circulation Disorders | Primary pulmonary hypertension | Diagnosis of Primary pulmonary hypertension |
| Pulmonary Circulation Disorders | Pulmonary embolism | Diagnosis of Pulmonary embolism |
| Pulmonary Circulation Disorders | Pulmonary embolism | History of Pulmonary embolism |
| Pulmonary Circulation Disorders | Pulmonary embolism | Procedure for Pulmonary embolism |

* * *

| Pulmonary Circulation Disorders | Secondary pulmonary hypertension | Diagnosis of Secondary pulmonary hypertension |
| --- | --- | --- |
| Rheumatoid Arthritis | Rheumatoid Arthritis | Diagnosis of Rheumatoid Arthritis |
| Rheumatoid Arthritis | Rheumatoid Arthritis | History of Rheumatoid Arthritis |
| Schizophrenia, schizotypal and delusional disorders | Schizophrenia, schizotypal and delusional disorders | Diagnosis of Schizophrenia, schizotypal and delusional disorders |
| Schizophrenia, schizotypal and delusional disorders | Schizophrenia, schizotypal and delusional disorders | History of Schizophrenia, schizotypal and delusional disorders |
| Stroke | Ischaemic stroke | Diagnosis of Ischaemic stroke |
| Stroke | Ischaemic stroke | History of cerebral infarction |
| Stroke | Ischaemic stroke | History of Ischaemic stroke |
| Stroke | Stroke NOS | Diagnosis of Stroke NOS |
| Stroke | Stroke NOS | History of Stroke NOS |
| Stroke | Stroke NOS | History of stroke, not specified as haemorrhage or infarction |
| Transient Ischaemic Attack | Transient ischaemic attack | Diagnosis of TIA |
| Transient Ischaemic Attack | Transient ischaemic attack | History of TIA |
| Visual Impairment and Blindness | Visual Impairment and Blindness | Diagnosis of blindness |
| Visual Impairment and Blindness | Visual Impairment and Blindness | Diagnosis of Visual impairment and blindness |

* * *

**Supplementary Table 4: Population details of the DataLoch dataset.**

| Feature | No. (%) |  |  |  |
| --- | --- | --- | --- | --- |
| Feature | Entire cohort(N=245614) | Non-FRI(N=227144) | FRI(N=18740) | P value |
| Age,mean(SD),y | 67.3(11.6) | 66.7(11.3) | 74.8(12.2) | <0.001 |
| SIMD quintiles |  |  |  |  |
| 1(least deprived) | 33365(13.6) | 30476(13.4) | 2889(15.6) | <0.001 |
| 2 | 53148(21.6) | 48612(21.4) | 4536(24.6) | <0.001 |
| 3 | 42130(17.2) | 39103(17.2) | 3027(16.4) | <0.001 |
| 4 | 42549(17.3) | 39347(17.3) | 3202(17.3) | <0.001 |
| 5 | 74422(30.3) | 69606(30.6) | 4816(26.1) | <0.001 |
| Smoking Status |  |  |  |  |
| Current smoker | 40192(16.4) | 37222(16.4) | 2970(16.1) | <0.001 |
| Ex-smoker | 115015(46.8) | 105870(46.6) | 9145(49.5) | <0.001 |
| Missing | 491(0.2) | 464(0.2) | 27(0.1) | <0.001 |
| Non-smoker | 89916(36.6) | 83588(36.8) | 6328(34.3) | <0.001 |
| EFI Value,mean(SD) | 0.1(0.1) | 0.1(0.1) | 0.2(0.1) | <0.001 |
| BMI |  |  |  |  |
| 0 | 7876(3.2) | 6804(3.0) | 1072(5.8) | <0.001 |
| 1 | 77450(31.5) | 70437(31.0) | 7013(38.0) | <0.001 |
| 2 | 85741(34.9) | 79968(35.2) | 5773(31.3) | <0.001 |
| 3 | 64319(26.2) | 60305(26.5) | 4014(21.7) | <0.001 |
| 4 | 10228(4.2) | 9630(4.2) | 598(3.2) | <0.001 |
| Alcohol Status |  |  |  |  |
| Alcohol intake above recommended sensible limits | 9302(3.8) | 8686(3.8) | 616(3.3) | <0.001 |
| Alcohol intake within recommended sensible limits | 63134(25.7) | 58752(25.9) | 4382(23.7) | <0.001 |
| Drinks rarely | 59027(24.0) | 54749(24.1) | 4278(23.2) | <0.001 |
| Heavy drinker-7-9u/day | 1889(0.8) | 1741(0.8) | 148(0.8) | <0.001 |
| Light drinker-1-2u/day | 20628(8.4) | 19394(8.5) | 1234(6.7) | <0.001 |
| Missing | 33348(13.6) | 31024(13.7) | 2324(12.6) | <0.001 |
| Moderate drinker-3-6u/day | 11477(4.7) | 10871(4.8) | 606(3.3) | <0.001 |
| Non-drinker alcohol | 45768(18.6) | 40984(18.0) | 4784(25.9) | <0.001 |
| Very heavy drinker->9u/day | 1041(0.4) | 943(0.4) | 98(0.5) | <0.001 |
| Ethnicity |  |  |  |  |
| Asian | 3444(1.4) | 3335(1.5) | 109(0.6) | <0.001 |
| Black | 891(0.4) | 870(0.4) | 21(0.1) | <0.001 |
| Missing | 21248(8.7) | 20486(9.0) | 762(4.1) | <0.001 |
| Mixed | 529(0.2) | 514(0.2) | 15(0.1) | <0.001 |
| Not Stated | 10784(4.4) | 10237(4.5) | 547(3.0) | <0.001 |
| Other | 1464(0.6) | 1412(0.6) | 52(0.3) | <0.001 |
| White | 207254(84.4) | 190290(83.8) | 16964(91.8) | <0.001 |
| Sex |  |  |  |  |
| Female | 114067(46.4) | 108327(47.7) | 5740(31.1) | <0.001 |

* * *

| Male | 131547(53.6) | 118817(52.3) | 12730(68.9) | <0.001 |
| --- | --- | --- | --- | --- |
| Medications |  |  |  |  |
| Thiazide and related diuretics | 34967(14.2) | 31891(14.0) | 3076(16.7) | <0.001 |
| Skeletal muscle relaxants | 2161(0.9) | 1968(0.9) | 193(1.0) | 0.014 |
| Selective serotonin reuptake inhibitors | 40490(16.5) | 37230(16.4) | 3260(17.7) | <0.001 |
| Other antidepressant drugs | 21211(8.6) | 19231(8.5) | 1980(10.7) | <0.001 |
| Other antianginal drugs | 3247(1.3) | 2881(1.3) | 366(2.0) | <0.001 |
| Opioid analgesics | 188237(76.6) | 174412(76.8) | 13825(74.9) | <0.001 |
| Non-steroidal anti-inflammatory drugs | 71078(28.9) | 67806(29.9) | 3272(17.7) | <0.001 |
| Nitrates | 23614(9.6) | 21456(9.4) | 2158(11.7) | <0.001 |
| Loop diuretics | 26056(10.6) | 22516(9.9) | 3540(19.2) | <0.001 |
| Hypnotics | 25630(10.4) | 23522(10.4) | 2108(11.4) | <0.001 |
| Drugs used in status epilepticus | 191(0.1) | 174(0.1) | 17(0.1) | 0.557 |
| Control of epilepsy | 31789(12.9) | 28972(12.8) | 2817(15.3) | <0.001 |
| Cardiac glycosides | 5632(2.3) | 4841(2.1) | 791(4.3) | <0.001 |
| Calcium-channel blockers | 57705(23.5) | 53056(23.4) | 4649(25.2) | <0.001 |
| Beta-adrenoceptor blocking drugs | 54345(22.1) | 49737(21.9) | 4608(24.9) | <0.001 |
| Anxiolytics | 30572(12.4) | 28508(12.6) | 2064(11.2) | <0.001 |
| Antispasmod.&other drgs.alt.gut motility | 24631(10.0) | 23336(10.3) | 1295(7.0) | <0.001 |
| Antipsychotic drugs | 11933(4.9) | 10990(4.8) | 943(5.1) | 0.108 |
| Antimuscarinic drugs used in parkin'ism | 620(0.3) | 543(0.2) | 77(0.4) | <0.001 |
| Antihistamines | 48350(19.7) | 45225(19.9) | 3125(16.9) | <0.001 |
| Angiotensin-ii receptor antagonists | 25941(10.6) | 23851(10.5) | 2090(11.3) | <0.001 |
| Angiotensin-converting enzyme inhibitors | 66644(27.1) | 61650(27.1) | 4994(27.0) | 0.769 |
| Alpha-adrenoceptor blocking drugs | 10494(4.3) | 9543(4.2) | 951(5.1) | <0.001 |
| Comorbidities |  |  |  |  |
| Visual impairment and blindness | 1320(0.5) | 1079(0.5) | 241(1.3) | <0.001 |
| Transient ischaemic attack | 4030(1.6) | 3632(1.6) | 398(2.2) | <0.001 |
| Stroke | 9822(4.0) | 8715(3.8) | 1107(6.0) | <0.001 |
| Schizophrenia, schizotypal and delusional disorders | 1134(0.5) | 1019(0.4) | 115(0.6) | <0.001 |
| Rheumatoid arthritis | 3186(1.3) | 2882(1.3) | 304(1.6) | <0.001 |
| Pulmonary circulation disorders | 22283(9.1) | 20173(8.9) | 2110(11.4) | <0.001 |
| Peripheral arterial disease | 4347(1.8) | 3985(1.8) | 362(2.0) | 0.045 |
| Parkinson's disease | 1302(0.5) | 1039(0.5) | 263(1.4) | <0.001 |
| Osteoporosis | 9487(3.9) | 6848(3.0) | 2639(14.3) | <0.001 |
| Myocardial infarction | 8033(3.3) | 7386(3.3) | 647(3.5) | 0.068 |

* * *

| Multiple valve dz | 1406(0.6) | 1215(0.5) | 191(1.0) | <0.001 |
| --- | --- | --- | --- | --- |
| Multiple sclerosis | 705(0.3) | 628(0.3) | 77(0.4) | <0.001 |
| Hyperthyroidism | 14250(5.8) | 13142(5.8) | 1108(6.0) | 0.240 |
| Hypertension | 52330(21.3) | 48262(21.2) | 4068(22.0) | 0.013 |
| Heart failure | 8071(3.3) | 7097(3.1) | 974(5.3) | <0.001 |
| Gout | 5374(2.2) | 4992(2.2) | 382(2.1) | 0.258 |
| Epilepsy | 2343(1.0) | 2049(0.9) | 294(1.6) | <0.001 |
| End stage renal disease | 911(0.4) | 841(0.4) | 70(0.4) | 0.900 |
| Diabetes mellitus | 20529(8.4) | 18729(8.2) | 1800(9.7) | <0.001 |
| Depression | 10896(4.4) | 10022(4.4) | 874(4.7) | 0.044 |
| Dementia | 10225(4.2) | 8032(3.5) | 2193(11.9) | <0.001 |
| Coronary | 20177(8.2) | 18429(8.1) | 1748(9.5) | <0.001 |
| Cancers | 27371(11.1) | 25484(11.2) | 1887(10.2) | <0.001 |
| Atrial fibrillation | 15717(6.4) | 13569(6.0) | 2148(11.6) | <0.001 |
| Asthma | 11805(4.8) | 11017(4.9) | 788(4.3) | <0.001 |
| Anxiety disorder | 7884(3.2) | 7298(3.2) | 586(3.2) | 0.782 |
| Angina | 8078(3.3) | 7409(3.3) | 669(3.6) | 0.009 |

* * *

# Supplementary Figure 1: Summary of recommendations generated by the Exploratory AI Recommender for the research question: Predict the risk of FRI.

| Feature Exclusion |  |
| --- | --- |
| alpha-adrenoceptor blocking drugs, antimuscarinic drugs used in Parkinism, cardiac glycosides, drugs used in status epilepticus, other antanginal drugs, other antidepressant drugs, selective serotonin re-uptake inhibitors, skeletal muscle relaxants, angina, anxiety disorder, depression, end stage renal disease, epilepsy, gout, multiple sclerosis, multiple valve dz, myocardial infarction, parkinson's disease, rheumatoid arthritis, schizophrenia schizotypal and delusional disorders, transient ischaemic attack, visual impairment and blindness |  |
| Model Non-linearity |  |
| Age, Alcohol |  |
| Feature Interactions |  |
| Stratified Variables | Interaction Variables |
| Age | asthma, atrial fibrillation, cancers, coronary, hypertension, pulmonary circulation disorders, stroke, alpha-adrenoceptor blocking drugs, angiotensin-II receptor antagonists, antihistamines, antispasmod&other drgs alt gut motility, beta-adrenoceptor blocking drugs, calcium-channel blockers, control of epilepsy, hypnotics, loop diuretics, nitrates, non-steroidal anti-inflammatory drugs, opioid analgesics, thiazides and related diuretics, sex, ethnicity, alcohol, EFI, smoking, simd2016 quintile |
| Ethnicity | asthma, atrial fibrillation, coronary, heart failure, hypertension, pulmonary circulation disorders, stroke, angiotensin-II receptor antagonists, antipsychotic drugs, antispasmod&other drgs alt gut motility, oxytolytics, calcium-channel blockers, hypnotics, opioid analgesics, thiazides and related diuretics, alcohol, BMI, EFI, smoking, simd2016 quintile |
| BMI | asthma, atrial fibrillation, cancers, coronary, diabetes mellitus, heart failure, hypertension, alpha-adrenoceptor blocking drugs, angiotensin-II receptor antagonists, antipsychotic drugs, beta-adrenoceptor blocking drugs, calcium-channel blockers, control of epilepsy, hypnotics, nitrates, opioid analgesics, thiazides and related diuretics, sex, EFI, smoking, simd2016 quintile, age |
| EFI | asthma, cancers, coronary, diabetes mellitus, heart failure, hypertension, hyperthyroidism, pulmonary circulation disorders, alpha-adrenoceptor blocking drugs, angiotensin-II receptor antagonists, antipsychotic drugs, antispasmod&other drgs alt gut motility, beta-adrenoceptor blocking drugs, calcium-channel blockers, hypnotics, loop diuretics, nitrates, opioid analgesics, sex, alcohol, simd2016\_sc quintile |
| Sex | asthma, cancers, coronary, diabetes mellitus, heart failure, hypertension, hyperthyroidism, pulmonary circulation disorders, alpha-adrenoceptor blocking drugs, angiotensin-II receptor antagonists, antipsychotic drugs, antispasmod&other drgs alt gut motility, beta-adrenoceptor blocking drugs, calcium-channel blockers, hypnotics, loop diuretics, nitrates, opioid analgesics, sex, alcohol, simd2016 quintile |
| Simd2016 Quintile | diabetes mellitus, heart failure, osteoporosis, peripheral arterial disease, pulmonary circulation disorders, alpha-adrenoceptor blocking drugs, antipsychotic drugs, antispasmod&other drgs alt gut motility, oxytolytics, |
| Loop Diuretics | atrial fibrillation, coronary, diabetes mellitus, heart failure, hypertension, antispasmod&other drgs alt gut motility, oxytolytics, beta-adrenoceptor blocking drugs, calcium-channel blockers, control of epilepsy, non-steroidal anti-inflammatory drugs, opioid analgesics, thiazides and related diuretics, sex, alcohol, BMI, smoking, simd2016 quintile |
| Dementia | diabetes mellitus, hypertension, hyperthyroidism, peripheral arterial disease, pulmonary circulation disorders, antihistamines, antispasmod&other drgs alt gut motility, beta-adrenoceptor blocking drugs, loop diuretics, non-steroidal anti-inflammatory drugs, thiazides and related diuretics, sex, ethnicity, alcohol, BMI, age |
| Non-steroidal anti-inflammatory drugs | asthma, coronary, hyperthyroidism, alpha-adrenoceptor blocking drugs, angiotensin-II receptor antagonists, antihistamines, antipsychotic drugs, antispasmod&other drgs alt gut motility, oxytolytics, beta-adrenoceptor blocking drugs, control of epilepsy, hypnotics, opioid analgesics, thiazides and related diuretics, sex, ethnicity, alcohol, BMI, EFI, smoking |
| Osteoporosis | diabetes mellitus, hypertension, antihistamines, antipsychotic drugs, antispasmod&other drgs alt gut motility, oxytolytics, beta-adrenoceptor blocking drugs, calcium-channel blockers, nitrates, non-steroidal anti-inflammatory drugs, opioid analgesics, sex, ethnicity, BMI, smoking, age |

* * *

## Supplementary Note 1: Feature Preprocessing

For the baseline model, we selected 58 features comprising sociodemographic characteristics,
lifestyle factors, frailty status, comorbidities, and medication use. Demographic variables
included age, sex, ethnicity, and Scottish Index of Multiple Deprivation (SIMD) quintile⁵⁶.
Lifestyle risk factors included smoking status, alcohol intake, and body mass index (BMI).
Frailty was assessed using the electronic Frailty Index (eFI) and categorized into 4 classes: not
57
frail, mild frailty, moderate frailty, and severe frailty. Comorbidities were determined from
either GP records (Read2), or hospital (ICD-10 codes recorded in Scottish Morbidity Records
\[SMR\]), using codelists developed by CALIBER and published in the Health Data Research
58
(HDR) UK phenotype library. To reduce redundancy and ensure focus on truly long-term
health conditions, we selected 153 CALIBER phenotypes of interest after clinical review, and
then grouped these into 27 long-term conditions (LTC) such as diabetes, ischaemic heart
disease, and depression and related disorders (see Supplementary Table 2 and Supplementary
Table 3). Medication classes of interest were defined by their British National Formulary (BNF)
paragraphs. Twenty-three medication classes were selected which have previously been
59–61
identified as Fall-Risk-Increasing Drugs (FRIDs), including alpha-adrenoceptor blocking
drugs, angiotensin-converting enzyme (ACE) inhibitors, angiotensin-II receptor antagonists,
antihistamines, antimuscarinic drugs used in parkinsonism, antipsychotic drugs,
antispasmodics and other drugs altering gut motility, anxiolytics, beta-adrenoceptor blocking
drugs, calcium-channel blockers, cardiac glycosides, drugs used for the control of epilepsy or
status epilepticus, hypnotics, loop diuretics, nitrates, NSAIDs, opioid analgesics, other
antianginal drugs, other antidepressant drugs, selective serotonin reuptake inhibitors (SSRIs),
skeletal muscle relaxants, and thiazide and related diuretics.

## Supplementary Note 2: Feature Attribution

Feature attribution is a technique from explainable AI that attempts to explain how the inputs
(clinical features) to a predictive model contribute to the output prediction. 62 There are a few
approaches to defining feature attributions, but the most common approach is based on the
concept of Shapley values from game theory. 15 Under the game-theoretic framework, a
prediction, such as the risk of a negative outcome, is considered like a monetary debt. Each of

responsible for this debt, and as such, each feature is expected to contribute a number of points
to the overall debt. Shapley values provide a mathematically formal way to compute how much
each feature contributed to the debt, and therefore how much they contribute to the prediction.

* * *

Shapley values can be used even if their underlying predictive model is complex and
63
nonlinear, which has made them a popular tool for explaining the behavior of AI models.

The absolute risk prediction considers the predicted risk 𝐹(𝑋) given a vector of observed
clinical features 𝑋 = (𝑥₁, …, 𝑥𝑀) for a certain patient. Clinical features, such as blood pressure,
are not alone indicative of risk, but rather it is deviations from their typical values that may
contribute to a risk prediction. Thus, we assume that for each clinical feature 𝑥𝑖, there is an
associated reference value 𝑥̃𝑖that encodes what we would expect to measure for an average
healthy patient, represented by the vector 𝑋̃ = (𝑥̃1, …, 𝑥̃𝑀). Baseline risk prediction considers
how the risk 𝐹(𝑋) of an individual 𝑋 differs from the risk of the reference individual 𝐹(𝑋̃).

$$
X=(x\_{1},\\ldots,x\_{M})
$$

$$
x\_{i}
$$

$$
{tilde{x}}\_{i}
$$

$$
\\tilde{X}=(\\tilde{x} _{1},\\dots,\\tilde{x}_{M})
$$

$$
F({\\tilde{X}})
$$

Depending on what kind of predictive model is used, different algorithms might be preferred
to calculate Shapley values. In this work, we compute Shapley values using the Kernel SHAP
64
algorithm. SHAP provides an efficient way to compute Shapley values for large models, since
the baseline definition is too computationally intensive to compute directly. Kernel SHAP is
particularly useful because it is widely applied, but also applicable to the tree-based models,
such as Random Survival Forest, studied in our work.

When the function 𝐹 for predicting the risk is known (or assumed), then one can directly apply
feature attribution methods to compute α𝑖. For additive models, various feature attribution
65
methods will yield the same result. However, the generalization of α𝑖to non-additive models
is not unique, and it requires a choice of definition. Generally, all such methods satisfy the
completeness equation:

$$
\\alpha\_{i}
$$

$$
\\alpha\_{i}
$$

(1)

$$
F(X)-F\\big({\\widetilde{X}}\\big)=\\sum\_{i=1}^{M}\\alpha\_{i},.
$$

Several popular approaches to feature attribution exist, and they differ in how they determine
α𝑖. The SHAP algorithm⁶⁴ is an extremely common choice, which extends the notion of Shapley
values from binary to continuous inputs. SHAP defines the attribution coefficients α𝑖to be

where ℱ is the set of all features, 𝐹(𝒮) is the model's predictions using only a subset 𝒮 ⊂ ℱ,
and \|𝒮\| is the number of elements in a set 𝒮. When specific model architectures are chosen,
there are specialized versions of the SHAP algorithm that allow SHAP values to be computed
64
more efficiently. Besides SHAP, there are several alternative methods for computing feature
66 62 17
attributions, including LIME, Integrated Gradients, SmoothGrad, and others.

$$
F(\\mathcal{S})
$$

$$
\\mathcal{F}
$$

$$
\\mathcal{S}
$$

$$
\\alpha\_{i}
$$

$$
\\alpha\_{i}
$$

$$
\\alpha\_{i}=\\sum\_{\\mathcal{S}\\subseteq\\mathcal{F}\\backslash i}\\frac{\|\\mathcal{S}\|!\\left(\|\\mathcal{F}\|-\|\\mathcal{S}\|-1\\right)!}{\|\\mathcal{F}\|!}\[F(\\mathcal{S}\\cup{i})-F(\\mathcal{S})\],
$$

* * *

There may be cases in which risk prediction is the goal, but there is no pre-established model
to work with. In this case, the model should be inferred using approaches from machine learning
and survival regression. Since many feature attribution methods are model agnostic, the choice
of model is very flexible. In our experiments, we learn the unknown function 𝐹 using a Random
Survival Forest²⁹ model. It offers robust predictions due to averaging over a number of survival
trees, each fitted on different sub-samples of the data (sub-sample size matches the original
dataset but the samples are drawn with replacement).