# =============================================================================
# CARDIOVASCULAR RISK AI — STREAMLIT APP (v6 — Complete Redesign)
# Dark navy + teal accents, elegant serif typography, modern layout
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="CardioAI — Clinical Decision Support",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------
# STYLING — Dark navy + teal, serif typography
# -----------------------------------------------------------------------

st.markdown("""
<style>
    /* ---- Google Fonts: elegant serif + clean sans ---- */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* ---- Root colors ---- */
    :root {
        --bg-dark: #0a1628;
        --bg-panel: #0f1e33;
        --bg-card: #142943;
        --teal: #5eead4;
        --teal-bright: #6ee7d0;
        --teal-dim: rgba(94, 234, 212, 0.15);
        --text-primary: #ffffff;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --border: rgba(94, 234, 212, 0.15);
    }
    
    /* ---- Main background with subtle grid ---- */
    .stApp {
        background-color: #0a1628;
        background-image: 
            linear-gradient(rgba(94, 234, 212, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(94, 234, 212, 0.03) 1px, transparent 1px);
        background-size: 60px 60px;
    }
    
    /* ---- Remove Streamlit default padding ---- */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    
    /* ---- Hide Streamlit branding ---- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {
        background: transparent;
    }
    
    /* ---- Typography ---- */
    html, body, [class*="css"], p, div, span, label, li {
        font-family: 'Inter', -apple-system, sans-serif !important;
        color: var(--text-primary) !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', Georgia, serif !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    
    /* ---- Navbar ---- */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0 2rem 0;
        border-bottom: 1px solid var(--border);
        margin-bottom: 3rem;
    }
    .navbar-logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
    }
    .logo-icon {
        width: 32px;
        height: 32px;
        background: var(--teal);
        border-radius: 8px;
        display: inline-block;
    }
    .navbar-links {
        display: flex;
        gap: 2.5rem;
        color: var(--text-secondary);
        font-size: 0.95rem;
    }
    .navbar-links a { color: var(--text-secondary); text-decoration: none; }
    .navbar-cta {
        background: var(--teal);
        color: #0a1628 !important;
        padding: 0.6rem 1.4rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* ---- Hero section ---- */
    .hero-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.4rem 1rem;
        border: 1px solid var(--teal);
        border-radius: 999px;
        color: var(--teal);
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .hero-pill::before {
        content: "";
        width: 6px; height: 6px;
        background: var(--teal);
        border-radius: 50%;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 4.5rem !important;
        line-height: 1.05 !important;
        font-weight: 700 !important;
        color: white !important;
        margin: 0 0 1.5rem 0 !important;
        letter-spacing: -0.03em;
    }
    .hero-title-accent {
        color: var(--teal) !important;
        font-style: italic;
        font-weight: 400 !important;
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--text-secondary) !important;
        max-width: 620px;
        margin-bottom: 2.5rem;
    }
    
    /* ---- Stats row ---- */
    .stats-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
        padding: 2rem 0;
        border-top: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
        margin: 3rem 0;
    }
    .stat-item { text-align: center; }
    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: var(--teal);
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    .stat-label {
        color: var(--text-secondary);
        font-size: 0.85rem;
        line-height: 1.4;
    }
    
    /* ---- Section labels ---- */
    .section-label {
        color: var(--teal);
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .section-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.8rem !important;
        color: white !important;
        line-height: 1.15 !important;
        margin-bottom: 1.5rem !important;
    }
    .section-subtitle {
        font-size: 1.05rem;
        color: var(--text-secondary);
        line-height: 1.7;
        max-width: 700px;
        margin-bottom: 3rem;
    }
    
    /* ---- Feature cards ---- */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        padding: 2rem;
        background: var(--bg-panel);
        border: 1px solid var(--border);
        border-radius: 16px;
        margin: 2rem 0;
    }
    .feature-card {
        padding: 1.5rem;
    }
    .feature-icon {
        width: 48px;
        height: 48px;
        background: var(--teal-dim);
        border: 1px solid var(--border);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem;
        color: white;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    .feature-desc {
        color: var(--text-secondary);
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* ---- Primary CTA button ---- */
    .stButton > button {
        background: var(--teal) !important;
        color: #0a1628 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.9rem 2rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.2s !important;
        letter-spacing: 0.01em;
    }
    .stButton > button:hover {
        background: var(--teal-bright) !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(94, 234, 212, 0.25);
    }
    .stButton > button * { color: #0a1628 !important; }
    
    /* ---- Input fields ---- */
    .stTextInput input, .stNumberInput input {
        background: var(--bg-card) !important;
        color: white !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        padding: 0.6rem 0.9rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus {
        border-color: var(--teal) !important;
        box-shadow: 0 0 0 3px var(--teal-dim) !important;
    }
    .stTextInput label, .stNumberInput label, .stSelectbox label, .stRadio label {
        color: var(--text-secondary) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }
    
    /* ---- Dropdowns ---- */
    div[data-baseweb="select"] > div {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: white !important;
    }
    div[data-baseweb="select"] * {
        color: white !important;
        font-family: 'Inter', sans-serif !important;
    }
    div[role="listbox"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
    }
    div[role="listbox"] * {
        color: white !important;
        background: var(--bg-card) !important;
    }
    div[role="option"]:hover {
        background: var(--teal-dim) !important;
    }
    
    /* ---- Radio buttons ---- */
    .stRadio [role="radiogroup"] {
        gap: 1rem;
    }
    .stRadio [role="radiogroup"] > label {
        background: var(--bg-panel);
        padding: 0.75rem 1.25rem;
        border-radius: 10px;
        border: 1px solid var(--border);
    }
    
    /* ---- Tabs ---- */
    .stTabs [data-baseweb="tab-list"] {
        background: transparent;
        border-bottom: 1px solid var(--border);
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: var(--text-secondary) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        padding: 0.75rem 0 !important;
        border-bottom: 2px solid transparent !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--teal) !important;
        border-bottom-color: var(--teal) !important;
    }
    .stTabs [aria-selected="true"] * { color: var(--teal) !important; }
    
    /* ---- Alerts ---- */
    .stAlert {
        background: var(--bg-panel) !important;
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
    }
    .stAlert * { color: var(--text-primary) !important; }
    
    /* ---- Progress bar ---- */
    .stProgress > div > div > div {
        background: var(--teal) !important;
    }
    .stProgress > div > div {
        background: var(--bg-card) !important;
    }
    
    /* ---- File uploader ---- */
    [data-testid="stFileUploaderDropzone"] {
        background: var(--bg-panel) !important;
        border: 2px dashed var(--border) !important;
        border-radius: 10px !important;
    }
    [data-testid="stFileUploaderDropzone"] * {
        color: var(--text-secondary) !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stFileUploaderDropzone"] button {
        background: var(--teal) !important;
        color: #0a1628 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.2rem !important;
        font-weight: 600 !important;
    }
    [data-testid="stFileUploaderDropzone"] button p { color: #0a1628 !important; }
    [data-testid="stFileUploaderDropzone"] button span.material-icons,
    [data-testid="stFileUploaderDropzone"] button span[class*="material"] {
        display: none !important;
    }
    .stFileUploader label {
        color: var(--text-secondary) !important;
    }
    
    /* ---- Result cards ---- */
    .result-card {
        background: var(--bg-panel);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
    }
    .risk-score-huge {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 700;
        line-height: 1;
        margin: 0.5rem 0;
    }
    
    /* ---- Citations ---- */
    .citation-block {
        background: var(--bg-panel);
        border-left: 3px solid var(--teal);
        padding: 1.5rem 2rem;
        border-radius: 8px;
        margin: 1.5rem 0;
        font-size: 0.9rem;
        line-height: 1.7;
        color: var(--text-secondary);
    }
    .citation-block * { color: var(--text-secondary) !important; }
    
    /* ---- Divider ---- */
    hr {
        border: none;
        border-top: 1px solid var(--border);
        margin: 3rem 0;
    }
    
    /* ---- Sidebar (kept hidden but styled if opened) ---- */
    section[data-testid="stSidebar"] {
        background: var(--bg-panel);
    }
    section[data-testid="stSidebar"] * { color: white !important; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------
# LOAD MODELS
# -----------------------------------------------------------------------

@st.cache_resource
def load_models():
    base = os.path.dirname(os.path.abspath(__file__))
    gene_pipeline = joblib.load(os.path.join(base, "cardio_pipeline.pkl"))
    encoder = joblib.load(os.path.join(base, "label_encoder.pkl"))
    gene_cols = joblib.load(os.path.join(base, "gene_columns.pkl"))
    clin_cols = joblib.load(os.path.join(base, "clinical_columns.pkl"))
    clinical_model = joblib.load(os.path.join(base, "clinical_only_model.pkl"))
    clinical_features = joblib.load(os.path.join(base, "clinical_feature_names.pkl"))
    return gene_pipeline, encoder, gene_cols, clin_cols, clinical_model, clinical_features

try:
    (gene_pipeline, encoder, GENE_COLUMNS, CLIN_COLUMNS,
     clinical_model, CLINICAL_FEATURES) = load_models()
    model_loaded = True
except FileNotFoundError as e:
    model_loaded = False
    load_error = str(e)

# -----------------------------------------------------------------------
# NAVBAR
# -----------------------------------------------------------------------

st.markdown("""
<div class="navbar">
    <div class="navbar-logo">
        <span class="logo-icon"></span>
        CardioAI
    </div>
    <div class="navbar-links">
        <a href="#features">Features</a>
        <a href="#screening">Screening Tool</a>
        <a href="#about">About</a>
    </div>
    <div><a href="#screening" class="navbar-cta">Start Screening</a></div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------------------

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
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------
# STATS ROW
# -----------------------------------------------------------------------

st.markdown("""
<div class="stats-row">
    <div class="stat-item">
        <div class="stat-number">17.9M</div>
        <div class="stat-label">Annual deaths from cardiovascular disease worldwide (WHO)</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">70K+</div>
        <div class="stat-label">Patients in the clinical training cohort</div>
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

# -----------------------------------------------------------------------
# WHAT THIS TOOL DOES
# -----------------------------------------------------------------------

st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">What This Tool Does</div>
    <h2 class="section-title">A faster path to clinical<br>clarity on heart risk</h2>
    <p class="section-subtitle">
        Cardiovascular disease is often silent until symptoms appear late. 
        This tool provides a reproducible, scored risk assessment in minutes — 
        using either lifestyle factors alone or full gene expression profiles 
        when available.
    </p>
</div>

<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Risk stratification</div>
        <div class="feature-desc">
            Composite 0–100 risk score weighted across demographics, vitals, 
            labs, and lifestyle factors — with per-factor breakdowns.
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
            Built on peer-reviewed cardiology research and public datasets. 
            A decision-support adjunct — not a replacement for clinical judgment.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if not model_loaded:
    st.error(f"❌ Could not load model files. Error: {load_error}")
    st.stop()

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------
# TABS — Screening tool & Learn
# -----------------------------------------------------------------------

st.markdown('<div id="screening"></div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Screening Tool", "Clinical Reference"])

# ========================================================
# TAB 1 — SCREENING
# ========================================================

with tab1:
    st.markdown("""
    <div class="section-label" style="margin-top:2rem;">Screening Tool</div>
    <h2 class="section-title">Begin assessment</h2>
    <p class="section-subtitle">
        Choose your input mode below. Clinical mode uses lifestyle and 
        vital-sign inputs. Genomic mode requires a normalized gene expression CSV.
    </p>
    """, unsafe_allow_html=True)
    
    input_mode = st.radio(
        "",
        ["Clinical / Lifestyle", "Gene Expression"],
        horizontal=True,
        label_visibility="collapsed",
    )
    use_gene_mode = "Gene" in input_mode
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # --------- CLINICAL MODE ---------
    if not use_gene_mode:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Demographics**")
            age = st.number_input("Age (years)", 18, 100, 50)
            gender_label = st.selectbox("Gender", ["Female", "Male"])
            gender = 1 if gender_label == "Female" else 2
            height = st.number_input("Height (cm)", 100, 220, 170)
            weight = st.number_input("Weight (kg)", 30, 250, 75)
            bmi = weight / ((height / 100) ** 2)
            st.markdown(f"<div style='color:var(--teal); font-weight:600; margin-top:0.5rem;'>BMI: {bmi:.1f}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Vitals & Labs**")
            ap_hi = st.number_input("Systolic BP (mmHg)", 70, 250, 120)
            ap_lo = st.number_input("Diastolic BP (mmHg)", 40, 200, 80)
            chol_label = st.selectbox("Cholesterol Level", ["Normal", "Above Normal", "Well Above Normal"])
            cholesterol = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[chol_label]
            gluc_label = st.selectbox("Glucose Level", ["Normal", "Above Normal", "Well Above Normal"])
            gluc = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[gluc_label]
        
        with col3:
            st.markdown("**Lifestyle**")
            smoke = 1 if st.selectbox("Smoking", ["No", "Yes"]) == "Yes" else 0
            alco = 1 if st.selectbox("Alcohol intake", ["No", "Yes"]) == "Yes" else 0
            active = 1 if st.selectbox("Physically active", ["Yes", "No"]) == "Yes" else 0
    
    # --------- GENE MODE ---------
    else:
        st.markdown("""
        Upload a CSV where each row is a sample and each column is a gene symbol 
        (e.g. TP53, IL6, BRCA1). Values should be normalized expression (log2 or z-score).
        """)
        uploaded_file = st.file_uploader("Gene expression CSV", type=["csv"])
        gene_data = None
        if uploaded_file:
            gene_data = pd.read_csv(uploaded_file, index_col=0)
            st.success(f"Loaded {gene_data.shape[0]} sample(s), {gene_data.shape[1]} genes")
    
    st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)
    
    # --------- PREDICT ---------
    if st.button("Begin Assessment →", type="primary"):
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)
        
        if not use_gene_mode:
            clin_input = pd.DataFrame([{
                "age_years": age, "gender": gender, "bmi": bmi,
                "ap_hi": ap_hi, "ap_lo": ap_lo,
                "cholesterol": cholesterol, "gluc": gluc,
                "smoke": smoke, "alco": alco, "active": active,
            }])[CLINICAL_FEATURES]
            
            prob = clinical_model.predict_proba(clin_input)[0]
            risk = prob[1] * 100
            
            if risk < 30:
                level, color = "Low Risk", "#5eead4"
            elif risk < 60:
                level, color = "Moderate Risk", "#fbbf24"
            else:
                level, color = "High Risk", "#f87171"
            
            st.markdown(f"""
            <div class="result-card">
                <div style="color: var(--text-secondary); font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase;">
                    Overall Cardiovascular Risk
                </div>
                <div class="risk-score-huge" style="color: {color};">{risk:.1f}%</div>
                <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: {color}; font-style: italic;">
                    {level}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.progress(int(risk))
            
            # Contributing factors
            st.markdown("<h3 style='margin-top: 2rem;'>Contributing Factors</h3>", unsafe_allow_html=True)
            factors = []
            if age > 55: factors.append(f"Age {age} — elevated risk after 55")
            if bmi > 30: factors.append(f"BMI {bmi:.1f} — obese range")
            elif bmi > 25: factors.append(f"BMI {bmi:.1f} — overweight range")
            if ap_hi >= 140 or ap_lo >= 90: factors.append(f"Blood pressure {ap_hi}/{ap_lo} — hypertensive range")
            if cholesterol >= 2: factors.append("Elevated cholesterol level")
            if gluc >= 2: factors.append("Elevated glucose level")
            if smoke: factors.append("Active smoker")
            if not active: factors.append("Sedentary lifestyle")
            
            if factors:
                for f in factors:
                    st.markdown(f"<div style='padding: 0.5rem 0; color: var(--text-secondary); border-bottom: 1px solid var(--border);'>→ {f}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div style='color: var(--teal); padding: 1rem 0;'>No major modifiable risk factors identified.</div>", unsafe_allow_html=True)
        
        else:
            if gene_data is None:
                st.warning("Please upload a gene expression CSV.")
                st.stop()
            
            for idx in gene_data.index:
                st.markdown(f"<h3>Sample: {idx}</h3>", unsafe_allow_html=True)
                gene_vector = pd.Series(0.0, index=GENE_COLUMNS)
                for gene in GENE_COLUMNS:
                    if gene in gene_data.columns:
                        gene_vector[gene] = gene_data.loc[idx, gene]
                clin_vector = pd.Series(0.0, index=CLIN_COLUMNS)
                X_input = pd.DataFrame([pd.concat([gene_vector, clin_vector])])
                probs = gene_pipeline.predict_proba(X_input)[0]
                
                for cls, p in zip(encoder.classes_, probs):
                    pct = p * 100
                    color = "#5eead4" if cls == "Healthy" else ("#fbbf24" if cls == "CAD" else "#f87171")
                    st.markdown(f"""
                    <div class="result-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div style="font-family: 'Playfair Display', serif; font-size: 1.4rem;">{cls}</div>
                            <div style="font-family: 'Playfair Display', serif; font-size: 2rem; color: {color};">{pct:.1f}%</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(pct))
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.info("Research and educational tool only. Not validated for clinical diagnosis. Consult a qualified healthcare professional.")

# ========================================================
# TAB 2 — CLINICAL REFERENCE
# ========================================================

with tab2:
    st.markdown("""
    <div class="section-label" style="margin-top: 2rem;">Clinical Reference</div>
    <h2 class="section-title">Understanding<br>cardiovascular disease</h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Cardiovascular diseases (CVDs) are the **leading cause of death worldwide**, 
    responsible for an estimated 17.9 million deaths each year, according to the 
    World Health Organization [1]. This tool focuses on three key outcomes: 
    **Coronary Artery Disease**, **Heart Failure**, and **general cardiovascular risk**.
    """)
    
    st.markdown("### Coronary Artery Disease (CAD)")
    st.markdown("""
    Coronary Artery Disease is caused by the buildup of atherosclerotic plaque 
    inside the coronary arteries that supply blood to the heart muscle. Over time, 
    these plaques narrow the artery walls, reducing oxygen delivery and potentially 
    leading to angina, myocardial infarction, or sudden cardiac death [2]. CAD is 
    often silent for decades before symptoms appear, making early risk assessment 
    critical. Major risk factors include hypertension, high LDL cholesterol, 
    smoking, diabetes, obesity, family history, and physical inactivity [3].
    
    Research using **blood-based gene expression profiling** has identified 
    inflammatory and immune-cell transcriptional signatures that distinguish CAD 
    patients from healthy controls, even before overt symptoms develop [4][5].
    """)
    
    st.markdown("### Heart Failure (HF)")
    st.markdown("""
    Heart Failure is a chronic, progressive condition affecting over 64 million 
    people globally [6]. It results from structural or functional cardiac 
    abnormalities — commonly following myocardial infarction, chronic hypertension, 
    or valvular disease. Symptoms include shortness of breath, fatigue, and 
    reduced exercise tolerance [7].
    
    The GSE59867 dataset used in this tool's genomic model tracks post-STEMI 
    patients across four timepoints and identifies transcriptomic signatures that 
    predict which patients progress to HF versus recover normally [8]. Early 
    identification enables earlier interventions such as beta-blockers, ACE 
    inhibitors, and SGLT2 inhibitors, which reduce HF-related mortality [9].
    """)
    
    st.markdown("### General Cardiovascular Risk")
    st.markdown("""
    Established risk calculators like the **ASCVD Risk Estimator** and 
    **Framingham Risk Score** use variables such as age, sex, blood pressure, 
    cholesterol, smoking status, and diabetes to stratify patients [10]. This 
    tool's clinical model is trained on the Kaggle Cardiovascular Disease dataset 
    (70,000 patients).
    
    The **INTERHEART study** [11] found that nine modifiable risk factors account 
    for over **90% of the population-attributable risk of a first myocardial 
    infarction** worldwide. Prevention remains the most powerful intervention.
    """)
    
    st.markdown("### The Role of AI in Cardiology")
    st.markdown("""
    Machine learning models combine high-dimensional biological data with 
    clinical measurements to detect patterns invisible to traditional statistical 
    methods. AI-based risk stratification can outperform conventional risk scores 
    in specific populations [12], particularly when integrating multi-omic and 
    lifestyle data. Ongoing challenges include dataset diversity, 
    interpretability, and prospective validation before clinical deployment [13].
    """)
    
    st.markdown("<h3 style='margin-top: 3rem;'>Works Cited</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="citation-block">
    [1] World Health Organization. (2021). <i>Cardiovascular diseases (CVDs)</i>.<br><br>
    [2] Libby, P., et al. (2019). Atherosclerosis. <i>Nature Reviews Disease Primers</i>, 5(1), 56.<br><br>
    [3] Arnett, D. K., et al. (2019). 2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease. <i>Circulation</i>, 140(11), e596–e646.<br><br>
    [4] Elashoff, M. R., et al. (2011). Blood-based gene expression algorithm for obstructive CAD. <i>BMC Medical Genomics</i>, 4, 26.<br><br>
    [5] Sinnaeve, P. R., et al. (2009). Gene expression patterns in peripheral blood correlate with CAD extent. <i>PLoS ONE</i>, 4(9), e7037.<br><br>
    [6] Groenewegen, A., et al. (2020). Epidemiology of heart failure. <i>European Journal of Heart Failure</i>, 22(8), 1342–1356.<br><br>
    [7] McDonagh, T. A., et al. (2021). 2021 ESC Guidelines for heart failure. <i>European Heart Journal</i>, 42(36), 3599–3726.<br><br>
    [8] Maciejak, A., et al. (2015). Gene expression profiling in heart failure progression. <i>Genome Medicine</i>, 7, 26.<br><br>
    [9] Zannad, F., et al. (2020). SGLT2 inhibitors in heart failure. <i>The Lancet</i>, 396(10254), 819–829.<br><br>
    [10] Goff, D. C., et al. (2014). ACC/AHA cardiovascular risk assessment guideline. <i>Circulation</i>, 129(25 suppl 2), S49–S73.<br><br>
    [11] Yusuf, S., et al. (2004). INTERHEART study: modifiable risk factors for MI. <i>The Lancet</i>, 364(9438), 937–952.<br><br>
    [12] Weng, S. F., et al. (2017). Machine-learning for cardiovascular risk prediction. <i>PLoS ONE</i>, 12(4), e0174944.<br><br>
    [13] Krittanawong, C., et al. (2020). Machine learning in cardiovascular diseases: meta-analysis. <i>Scientific Reports</i>, 10, 16057.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------

st.markdown("""
<div style="margin-top: 5rem; padding: 2rem 0; border-top: 1px solid var(--border); text-align: center; color: var(--text-muted); font-size: 0.85rem;">
    CardioAI — Research & educational tool. Not a diagnostic device.<br>
    © 2025 — Built with clinical decision support in mind.
</div>
""", unsafe_allow_html=True)
