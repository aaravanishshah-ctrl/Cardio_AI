# =============================================================================
# CardioAI — SCREENING TOOL PAGE
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from styles import apply_styles, render_navbar, render_footer

st.set_page_config(
    page_title="Screening Tool — CardioAI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()
render_navbar(active_page="screening")

# LOAD MODELS
@st.cache_resource
def load_models():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
except FileNotFoundError as e:
    st.error(f"Could not load model files: {e}")
    st.stop()

# HEADER
st.markdown("""
<div style="padding: 2rem 0;">
    <div class="section-label">Screening Tool</div>
    <h1 class="hero-title" style="font-size: 3.5rem;">Begin <span class="hero-title-accent">assessment.</span></h1>
    <p class="hero-subtitle">
        Choose your input mode below. Clinical mode uses lifestyle and 
        vital-sign inputs. Genomic mode requires a normalized gene expression CSV.
    </p>
</div>
""", unsafe_allow_html=True)

input_mode = st.radio(
    "",
    ["Clinical / Lifestyle", "Gene Expression"],
    horizontal=True,
    label_visibility="collapsed",
)
use_gene_mode = "Gene" in input_mode
st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

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
        st.markdown(f"<div style='color:#5eead4; font-weight:600; margin-top:0.5rem;'>BMI: {bmi:.1f}</div>", unsafe_allow_html=True)
    
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
else:
    st.markdown("""
    Upload a CSV where each row is a sample and each column is a gene symbol 
    (e.g. TP53, IL6). Values should be normalized (log2 or z-score).
    """)
    uploaded_file = st.file_uploader("Gene expression CSV", type=["csv"])
    gene_data = None
    if uploaded_file:
        gene_data = pd.read_csv(uploaded_file, index_col=0)
        st.success(f"Loaded {gene_data.shape[0]} sample(s), {gene_data.shape[1]} genes")

st.markdown("<div style='margin: 2rem 0;'></div>", unsafe_allow_html=True)

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
            <div style="color: #94a3b8; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase;">
                Overall Cardiovascular Risk
            </div>
            <div class="risk-score-huge" style="color: {color};">{risk:.1f}%</div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; color: {color}; font-style: italic;">
                {level}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(int(risk))
        
        st.markdown("<h3 style='margin-top: 2rem;'>Contributing Factors</h3>", unsafe_allow_html=True)
        factors = []
        if age > 55: factors.append(f"Age {age} — elevated risk after 55")
        if bmi > 30: factors.append(f"BMI {bmi:.1f} — obese range")
        elif bmi > 25: factors.append(f"BMI {bmi:.1f} — overweight range")
        if ap_hi >= 140 or ap_lo >= 90: factors.append(f"BP {ap_hi}/{ap_lo} — hypertensive range")
        if cholesterol >= 2: factors.append("Elevated cholesterol level")
        if gluc >= 2: factors.append("Elevated glucose level")
        if smoke: factors.append("Active smoker")
        if not active: factors.append("Sedentary lifestyle")
        
        if factors:
            for f in factors:
                st.markdown(f"<div style='padding: 0.5rem 0; color: #94a3b8; border-bottom: 1px solid rgba(94, 234, 212, 0.15);'>→ {f}</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='color: #5eead4; padding: 1rem 0;'>No major modifiable risk factors identified.</div>", unsafe_allow_html=True)
    
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
    st.info("Research and educational tool only. Not validated for clinical diagnosis.")

render_footer()
