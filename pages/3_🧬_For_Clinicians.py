# =============================================================================
# CardioAI — FOR CLINICIANS PAGE (technical / methodology)
# =============================================================================

import streamlit as st
from styles import apply_styles, render_navbar, render_footer

st.set_page_config(page_title="For Clinicians — CardioAI", page_icon="🧬", layout="wide", initial_sidebar_state="collapsed")
apply_styles()
render_navbar(active_page="clinicians")

st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">For Clinicians</div>
    <h1 class="hero-title" style="font-size: 3.5rem;">Methodology &<br><span class="hero-title-accent">model architecture.</span></h1>
    <p class="hero-subtitle">
        Technical documentation on how CardioAI's models are trained, validated, 
        and intended to be used in clinical decision-support workflows.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Model Architecture")
st.markdown("""
CardioAI uses two independently trained models depending on input mode:

**Clinical Model (XGBoost)** — trained on the Kaggle Cardiovascular Disease 
dataset (n=70,000, positive rate ~50%). Features include age, gender, BMI, 
systolic/diastolic BP, cholesterol level (categorical 1-3), glucose level 
(categorical 1-3), smoking status, alcohol intake, and physical activity. 
Preprocessing: median imputation for missing values, StandardScaler 
normalization. Training: 80/20 stratified split, 300 trees, max depth 5, 
learning rate 0.05.

**Genomic Model (XGBoost multiclass)** — trained on NCBI GEO series GSE20680 
and GSE20681 (CAD, n=~200 each) and GSE59867 (Heart Failure progression, 
n=34 confirmed HF patients across timepoints). Preprocessing: log2 
transformation, per-dataset z-score normalization for batch effect 
correction, then intersection to ~16,000 common gene symbols across 
platforms. Feature selection: top 500 genes by ANOVA F-score (SelectKBest).
""")

st.markdown("### Performance Metrics")
st.markdown("""
| Model | Accuracy | ROC AUC | Test Set Size |
|---|---|---|---|
| Clinical (XGBoost) | ~0.73 | ~0.80 | 13,919 patients |
| Genomic (XGBoost) | ~0.65 | — | 86 samples |

The clinical model's performance is comparable to published lifestyle-based 
risk calculators. The genomic model has substantially smaller sample size 
(particularly for Heart Failure, n=34), and results should be interpreted 
as preliminary. Cross-validation F1-macro for the genomic model averages 
~0.46 across 5 folds, with high variance between folds.
""")

st.markdown("### Intended Use")
st.markdown("""
CardioAI is designed as a **decision-support adjunct** for:
- Preliminary risk stratification during initial patient assessment
- Identifying patients who may benefit from expedited cardiology referral
- Educational demonstration of AI-driven risk modeling
- Research applications combining transcriptomic and clinical data

**Not intended for:**
- Sole basis for diagnosis or treatment decisions
- Emergency triage
- Replacing validated clinical risk scores (ASCVD, Framingham) in guideline-directed care
- Pediatric or pregnant populations (training data was adult non-pregnant)
""")

st.markdown("### Known Limitations")
st.markdown("""
- **Dataset demographics**: The clinical training cohort is predominantly 
European. Performance in other populations has not been validated.
- **Genomic sample size**: The Heart Failure class in the genomic model 
draws from a single study (GSE59867), limiting generalizability.
- **No temporal validation**: Models were trained and tested on 
cross-sectional data. Longitudinal predictive performance is untested.
- **Feature availability**: Some risk factors that appear in guidelines 
(family history, LDL/HDL breakdown, hs-CRP) are not present in the training 
data and cannot be incorporated by this tool.
- **Regulatory status**: This tool has not been reviewed by the FDA or 
equivalent regulatory bodies and should not be marketed as a medical device.
""")

st.markdown("### Data Provenance")
st.markdown("""
- **Kaggle Cardiovascular Disease Dataset** — Public domain, 70,000 patient records
- **NCBI GEO GSE20680, GSE20681** — Peripheral blood microarray, CAD case-control
- **NCBI GEO GSE59867** — Post-STEMI longitudinal transcriptomics, HF progression
""")

render_footer()
