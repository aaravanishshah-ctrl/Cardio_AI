# =============================================================================
# CardioAI — ABOUT PAGE
# =============================================================================

import streamlit as st
from styles import apply_styles, render_navbar, render_footer

st.set_page_config(page_title="About — CardioAI", page_icon="ℹ️", layout="wide", initial_sidebar_state="collapsed")
apply_styles()
render_navbar(active_page="about")

st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">About</div>
    <h1 class="hero-title" style="font-size: 3.5rem;">About <span class="hero-title-accent">CardioAI.</span></h1>
    <p class="hero-subtitle">
        A student-built clinical decision-support project exploring the 
        integration of gene expression profiling with lifestyle-based 
        cardiovascular risk prediction.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### The Project")
st.markdown("""
CardioAI was developed as part of an internship research project focused on 
applying machine learning to publicly available biomedical datasets. The 
goal was to build a functional, deployable tool that demonstrates end-to-end 
ML workflow — from raw data ingestion (NCBI GEO), through preprocessing and 
model training, to deployment as a web application.
""")

st.markdown("### Technology Stack")
st.markdown("""
- **Backend / ML**: Python, scikit-learn, XGBoost, GEOparse, pandas
- **Frontend**: Streamlit with custom CSS
- **Deployment**: Streamlit Community Cloud, GitHub
- **Data sources**: NCBI Gene Expression Omnibus (GEO), Kaggle
""")

st.markdown("### Acknowledgments")
st.markdown("""
- NCBI GEO for providing open-access gene expression datasets
- The authors of GSE20680, GSE20681, and GSE59867 for making their data 
publicly available
- The Kaggle community for maintaining the Cardiovascular Disease dataset
- The open-source scientific Python ecosystem
""")

st.markdown("### Disclaimer")
st.markdown("""
This tool is a research and educational demonstration. It is **not a 
medical device**, has not undergone clinical validation, and should not be 
used to make medical decisions. All predictions are based on statistical 
patterns in training data and may not generalize to individual patients. 
Consult a qualified healthcare professional for medical advice.
""")

render_footer()
