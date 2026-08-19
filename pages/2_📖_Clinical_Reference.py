# =============================================================================
# CardioAI — CLINICAL REFERENCE PAGE
# =============================================================================

import streamlit as st
from styles import apply_styles, render_navbar, render_footer

st.set_page_config(page_title="Clinical Reference — CardioAI", page_icon="📖", layout="wide", initial_sidebar_state="collapsed")
apply_styles()
render_navbar(active_page="clinical")

st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">Clinical Reference</div>
    <h1 class="hero-title" style="font-size: 3.5rem;">Understanding<br>cardiovascular <span class="hero-title-accent">disease.</span></h1>
    <p class="hero-subtitle">
        A concise overview of the three conditions this tool addresses: 
        Coronary Artery Disease, Heart Failure, and general cardiovascular risk — 
        with primary literature references.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Coronary Artery Disease (CAD)")
st.markdown("""
Coronary Artery Disease is caused by the buildup of atherosclerotic plaque 
inside the coronary arteries. Over time, plaques narrow the artery walls, 
reducing oxygen delivery and potentially leading to angina, myocardial 
infarction, or sudden cardiac death [2]. CAD is often silent for decades 
before symptoms appear. Major risk factors include hypertension, high LDL 
cholesterol, smoking, diabetes, obesity, family history, and physical 
inactivity [3].

Blood-based gene expression profiling has identified inflammatory and 
immune-cell transcriptional signatures that distinguish CAD patients from 
healthy controls, even before overt symptoms develop [4][5].
""")

st.markdown("### Heart Failure (HF)")
st.markdown("""
Heart Failure is a chronic, progressive condition affecting over 64 million 
people globally [6]. It results from structural or functional cardiac 
abnormalities — commonly following myocardial infarction, chronic hypertension, 
or valvular disease. Symptoms include shortness of breath, fatigue, and 
reduced exercise tolerance [7].

The GSE59867 dataset used in this tool's genomic model tracks post-STEMI 
patients across four timepoints and identifies transcriptomic signatures 
predicting which patients progress to HF versus recover normally [8]. Early 
identification enables earlier interventions such as beta-blockers, ACE 
inhibitors, and SGLT2 inhibitors, which reduce HF-related mortality [9].
""")

st.markdown("### General Cardiovascular Risk")
st.markdown("""
Established risk calculators like the **ASCVD Risk Estimator** and 
**Framingham Risk Score** use variables such as age, sex, blood pressure, 
cholesterol, smoking status, and diabetes to stratify patients [10]. This 
tool's clinical model is trained on the Kaggle Cardiovascular Disease 
dataset (70,000 patients).

The **INTERHEART study** [11] found that nine modifiable risk factors 
account for over 90% of the population-attributable risk of a first 
myocardial infarction worldwide.
""")

st.markdown("<h3 style='margin-top: 3rem;'>Works Cited</h3>", unsafe_allow_html=True)
st.markdown("""
<div class="citation-block">
[1] World Health Organization. (2021). <i>Cardiovascular diseases (CVDs)</i>.<br><br>
[2] Libby, P., et al. (2019). Atherosclerosis. <i>Nature Reviews Disease Primers</i>, 5(1), 56.<br><br>
[3] Arnett, D. K., et al. (2019). 2019 ACC/AHA Guideline on Primary Prevention of CVD. <i>Circulation</i>, 140(11), e596–e646.<br><br>
[4] Elashoff, M. R., et al. (2011). Blood-based gene expression algorithm for CAD. <i>BMC Medical Genomics</i>, 4, 26.<br><br>
[5] Sinnaeve, P. R., et al. (2009). Peripheral blood gene expression and CAD extent. <i>PLoS ONE</i>, 4(9), e7037.<br><br>
[6] Groenewegen, A., et al. (2020). Epidemiology of heart failure. <i>European Journal of Heart Failure</i>, 22(8), 1342–1356.<br><br>
[7] McDonagh, T. A., et al. (2021). 2021 ESC Guidelines for heart failure. <i>European Heart Journal</i>, 42(36), 3599–3726.<br><br>
[8] Maciejak, A., et al. (2015). Gene expression profiling in HF progression. <i>Genome Medicine</i>, 7, 26.<br><br>
[9] Zannad, F., et al. (2020). SGLT2 inhibitors in HF. <i>The Lancet</i>, 396(10254), 819–829.<br><br>
[10] Goff, D. C., et al. (2014). ACC/AHA CVD risk assessment guideline. <i>Circulation</i>, 129(25 suppl 2), S49–S73.<br><br>
[11] Yusuf, S., et al. (2004). INTERHEART study: modifiable MI risk factors. <i>The Lancet</i>, 364(9438), 937–952.
</div>
""", unsafe_allow_html=True)

render_footer()
