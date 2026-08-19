# =============================================================================
# CardioAI — HOME PAGE
# =============================================================================

import streamlit as st
from styles import apply_styles, render_navbar, render_footer

st.set_page_config(
    page_title="CardioAI — Clinical Decision Support",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()
render_navbar(active_page="home")

# Handle hero button query params
if "goto" in st.query_params:
    target = st.query_params["goto"]
    st.query_params.clear()
    if target == "screening":
        st.switch_page("pages/1_Screening_Tool.py")
    elif target == "clinical":
        st.switch_page("pages/2_Clinical_Reference.py")

# HERO
st.markdown("""
<div style="padding: 3rem 0 2rem 0;">
    <div class="hero-pill">Clinical Decision Support</div>
    <h1 class="hero-title">
        Cardiovascular risk<br>
        prediction, <span class="hero-title-accent">refined.</span>
    </h1>
    <p class="hero-subtitle">
        An AI-powered clinical decision support tool combining lifestyle risk 
        modeling with blood-based gene expression profiling — built for clinicians 
        and researchers who need precision, speed, and clarity.
    </p>
    <div style="display: flex; gap: 1rem; margin-top: 2rem;">
        <a href="?goto=screening" target="_self" style="text-decoration:none;">
            <div style="background: #5eead4; color: #0a1628; padding: 0.9rem 2rem; border-radius: 10px; font-weight: 600; font-family: 'Inter', sans-serif; display: inline-block; cursor: pointer; transition: all 0.2s;"
                 onmouseover="this.style.background='#6ee7d0'; this.style.transform='translateY(-2px)';"
                 onmouseout="this.style.background='#5eead4'; this.style.transform='translateY(0)';">
                🕐 Begin Assessment
            </div>
        </a>
        <a href="?goto=clinical" target="_self" style="text-decoration:none;">
            <div style="background: transparent; color: white; padding: 0.9rem 2rem; border-radius: 10px; font-weight: 600; border: 1px solid rgba(94, 234, 212, 0.3); font-family: 'Inter', sans-serif; display: inline-block; cursor: pointer; transition: all 0.2s;"
                 onmouseover="this.style.background='rgba(94, 234, 212, 0.1)'; this.style.color='#5eead4';"
                 onmouseout="this.style.background='transparent'; this.style.color='white';">
                Explore features →
            </div>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown("""
<div class="stats-row">
    <div class="stat-item">
        <div class="stat-number">17.9M</div>
        <div class="stat-label">Annual CVD deaths worldwide (WHO)</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">70K+</div>
        <div class="stat-label">Patients in clinical training cohort</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">0.80</div>
        <div class="stat-label">ROC AUC on held-out test data</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">2</div>
        <div class="stat-label">Prediction modes: clinical & genomic</div>
    </div>
</div>
""", unsafe_allow_html=True)

# WHAT THIS TOOL DOES
st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">What This Tool Does</div>
    <h2 class="section-title">A faster path to clinical<br>clarity on heart risk</h2>
    <p class="section-subtitle">
        Cardiovascular disease is often silent until symptoms appear late. 
        This tool provides a reproducible, scored risk assessment in minutes — 
        using either lifestyle factors alone or full gene expression profiles.
    </p>
</div>

<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Risk stratification</div>
        <div class="feature-desc">
            Composite 0–100 risk score weighted across demographics, vitals, 
            labs, and lifestyle — with per-factor breakdowns.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🧬</div>
        <div class="feature-title">Genomic profiling</div>
        <div class="feature-desc">
            Classifies blood samples as CAD, Heart Failure, or Healthy using 
            transcriptomic signatures from NCBI GEO datasets.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📖</div>
        <div class="feature-title">Evidence-grounded</div>
        <div class="feature-desc">
            Built on peer-reviewed cardiology research. A decision-support 
            adjunct — not a replacement for clinical judgment.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

render_footer()
