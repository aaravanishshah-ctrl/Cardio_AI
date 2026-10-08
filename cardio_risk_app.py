# =============================================================================
# CardioAI — HOME PAGE (Landing Page - Clinical Theme)
# =============================================================================

import streamlit as st
from styles import apply_styles, render_footer, render_navbar

# 1. Page Configuration
st.set_page_config(
    page_title="CardioAI — Clinical Decision Support",
    page_icon="favicon.svg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Apply global styles and navigation bar
apply_styles()
render_navbar(active_page="home")

# 3. Handle fast-navigation routing for the Hero buttons
if "goto" in st.query_params:
  target = st.query_params["goto"]
  st.query_params.clear()
  if target == "screening":
    st.switch_page("pages/1_Screening_Tool.py")
  elif target == "clinical":
    st.switch_page("pages/2_Clinical_Reference.py")

# 4. HERO SECTION
st.markdown(
    """
<div style="padding: 2.5rem 0 1.5rem 0;">
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
            <div style="background: #1e40af; color: #ffffff; padding: 0.85rem 1.8rem; border-radius: 6px; font-weight: 600; font-family: 'Inter', sans-serif; display: inline-block; cursor: pointer; transition: all 0.15s ease; box-shadow: 0 1px 2px rgba(0,0,0,0.05);"
                 onmouseover="this.style.background='#1e3a8a';"
                 onmouseout="this.style.background='#1e40af';">
                Begin Assessment →
            </div>
        </a>
        <a href="?goto=clinical" target="_self" style="text-decoration:none;">
            <div style="background: #ffffff; color: #0f172a; padding: 0.85rem 1.8rem; border-radius: 6px; font-weight: 600; border: 1px solid #e2e8f0; font-family: 'Inter', sans-serif; display: inline-block; cursor: pointer; transition: all 0.15s ease; box-shadow: 0 1px 2px rgba(0,0,0,0.05);"
                 onmouseover="this.style.background='#f1f5f9'; this.style.borderColor='#bfdbfe';"
                 onmouseout="this.style.background='#ffffff'; this.style.borderColor='#e2e8f0';">
                Explore features
            </div>
        </a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# 5. STATS ROW
st.markdown(
    """
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
        <div class="stat-number">85.1%</div>
        <div class="stat-label">Multiclass accuracy on genomic test cohort</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">6</div>
        <div class="stat-label">Genomic diagnostic conditions evaluated</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# 6. WHAT THIS TOOL DOES / FEATURE GRID
st.markdown(
    """
<div style="padding: 1.5rem 0 0.5rem 0;">
    <div class="section-label">System Capabilities</div>
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
        <div class="feature-title">Risk Stratification</div>
        <div class="feature-desc">
            Composite 0–100 risk score weighted across demographics, vitals, 
            labs, and lifestyle — with rule-based per-condition breakdowns.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🧬</div>
        <div class="feature-title">Genomic Profiling</div>
        <div class="feature-desc">
            Classifies blood samples across 6 classes: CAD, Heart Failure, AFib, 
            Hypertension, Ischemic Stroke, or Healthy using NCBI GEO datasets.
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📖</div>
        <div class="feature-title">Evidence-Grounded</div>
        <div class="feature-desc">
            Built on peer-reviewed cardiology research. A decision-support 
            adjunct — not a replacement for clinical judgment.
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# 7. FOOTER
render_footer()
