# =============================================================================
# CARDIOVASCULAR RISK AI — STREAMLIT APP (v4)
# - Kaggle Cardio dataset for clinical prediction
# - Clinical fields ONLY shown in Clinical mode
# - Gene mode ONLY asks for CSV upload
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
    page_title="Cardiovascular Risk AI",
    page_icon="❤️",
    layout="wide",
)

# -----------------------------------------------------------------------
# STYLING
# -----------------------------------------------------------------------

st.markdown("""
<style>
    /* Main background — cerulean blue */
    .stApp {
        background: #007BA7;
    }
    
    /* Fonts — Georgia, white body text */
    html, body, [class*="css"], p, div, span, label {
        font-family: 'Georgia', serif !important;
        color: white !important;
    }
    
    /* Headers — dark blue */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Georgia', serif !important;
        color: #0a1f44 !important;
        font-weight: 700;
    }
    
    /* Input labels — white */
    .stTextInput label, .stNumberInput label, .stSelectbox label, 
    .stRadio label, .stFileUploader label {
        color: white !important;
    }
    
    /* Text inputs — white bg, black text */
    .stTextInput input, .stNumberInput input {
        color: #0a1f44 !important;
        background-color: white !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Dropdown — white bg, dark text */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: #0a1f44 !important;
    }
    div[data-baseweb="select"] * {
        color: #0a1f44 !important;
        font-family: 'Georgia', serif !important;
    }
    div[role="listbox"] {
        background-color: white !important;
    }
    div[role="listbox"] * {
        color: #0a1f44 !important;
        background-color: white !important;
        font-family: 'Georgia', serif !important;
    }
    div[role="option"]:hover {
        background-color: #cce7f0 !important;
    }
    
    /* Button — white bg, dark navy text */
    .stButton > button {
        background-color: white !important;
        color: #0a1f44 !important;
        border-radius: 10px;
        border: 2px solid #0a1f44;
        padding: 0.6rem 2rem;
        font-family: 'Georgia', serif !important;
        font-weight: 700;
        font-size: 1.05rem;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #f0f8ff !important;
        color: #0a1f44 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .stButton > button * {
        color: #0a1f44 !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0a1f44;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Alert boxes */
    .stAlert {
        background-color: white !important;
    }
    .stAlert * {
        color: #0a1f44 !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #0a1f44 !important;
    }
    
    /* File uploader */
    .stFileUploader > div {
        background-color: white !important;
        border-radius: 8px;
    }
    .stFileUploader label {
        color: white !important;
    }
    .stFileUploader * {
        color: #0a1f44 !important;
    }
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
# HEADER
# -----------------------------------------------------------------------

st.title("❤️ Cardiovascular Risk AI")
st.markdown("""
An AI-powered tool that estimates cardiovascular risk using either 
**clinical/lifestyle data** (validated) or **gene expression profiles** (research).
""")

if not model_loaded:
    st.error(f"❌ Could not load model files. Error: {load_error}")
    st.stop()

# -----------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------

with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **Two prediction modes:**
    
    🩺 **Clinical Mode**  
    Predicts overall cardiovascular disease risk from lifestyle 
    and clinical factors (age, BP, BMI, cholesterol, smoking, 
    activity level). Trained on 70,000 patients from the Kaggle 
    Cardiovascular Disease dataset.
    
    🧬 **Gene Expression Mode**  
    Uses blood gene expression profiles to classify samples as 
    CAD, Heart Failure, or Healthy. Trained on NCBI GEO 
    datasets (research-only).
    
    ---
    
    **⚠️ Disclaimer**  
    Research/educational tool. Not a diagnostic device.
    """)

# -----------------------------------------------------------------------
# INPUT MODE
# -----------------------------------------------------------------------

st.header("📋 Choose Input Mode")

input_mode = st.radio(
    "Prediction mode:",
    ["🩺 Clinical / Lifestyle (recommended)", "🧬 Gene Expression"],
    horizontal=True,
)

use_gene_mode = "Gene" in input_mode

st.markdown("---")

# =======================================================================
# CLINICAL MODE — Show lifestyle inputs
# =======================================================================

if not use_gene_mode:
    st.subheader("🩺 Lifestyle & Clinical Data")
    st.markdown("Fill in the fields below to estimate your cardiovascular risk.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Demographics**")
        age = st.number_input("Age (years)", 18, 100, 50)
        gender_label = st.selectbox("Gender", ["Female", "Male"])
        gender = 1 if gender_label == "Female" else 2
        height = st.number_input("Height (cm)", 100, 220, 170)
        weight = st.number_input("Weight (kg)", 30, 250, 75)
        bmi = weight / ((height / 100) ** 2)
        st.info(f"**BMI:** {bmi:.1f}")
    
    with col2:
        st.markdown("**Blood Pressure & Labs**")
        ap_hi = st.number_input("Systolic BP (mmHg)", 70, 250, 120)
        ap_lo = st.number_input("Diastolic BP (mmHg)", 40, 200, 80)
        
        chol_label = st.selectbox("Cholesterol Level", 
                                  ["Normal", "Above Normal", "Well Above Normal"])
        cholesterol = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[chol_label]
        
        gluc_label = st.selectbox("Glucose Level", 
                                  ["Normal", "Above Normal", "Well Above Normal"])
        gluc = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}[gluc_label]
    
    with col3:
        st.markdown("**Lifestyle**")
        smoke_label = st.selectbox("Do you smoke?", ["No", "Yes"])
        smoke = 1 if smoke_label == "Yes" else 0
        
        alco_label = st.selectbox("Alcohol intake?", ["No", "Yes"])
        alco = 1 if alco_label == "Yes" else 0
        
        active_label = st.selectbox("Physically active?", ["Yes", "No"])
        active = 1 if active_label == "Yes" else 0

# =======================================================================
# GENE MODE — Show only CSV upload
# =======================================================================

else:
    st.subheader("🧬 Gene Expression Upload")
    st.markdown("""
    Upload a **CSV file** where:
    - Each **row** is one sample (patient)
    - Each **column** is a gene symbol (e.g. `TP53`, `IL6`, `BRCA1`)
    - Values should be normalized expression (log2 or z-score)
    
    Genes not seen during training will be ignored. 
    Missing genes will be filled with 0.
    """)
    
    uploaded_file = st.file_uploader("Upload gene expression CSV", type=["csv"])
    gene_data = None
    if uploaded_file:
        gene_data = pd.read_csv(uploaded_file, index_col=0)
        st.success(f"✅ Loaded {gene_data.shape[0]} sample(s), {gene_data.shape[1]} genes")
        with st.expander("Preview data"):
            st.dataframe(gene_data.head(3))

# -----------------------------------------------------------------------
# PREDICT BUTTON
# -----------------------------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Cardiovascular Risk", type="primary", use_container_width=True):
    
    st.header("📊 Results")
    
    # ---------- CLINICAL MODE ----------
    if not use_gene_mode:
        clin_input = pd.DataFrame([{
            "age_years": age,
            "gender": gender,
            "bmi": bmi,
            "ap_hi": ap_hi,
            "ap_lo": ap_lo,
            "cholesterol": cholesterol,
            "gluc": gluc,
            "smoke": smoke,
            "alco": alco,
            "active": active,
        }])[CLINICAL_FEATURES]
        
        prob = clinical_model.predict_proba(clin_input)[0]
        risk = prob[1] * 100
        
        if risk < 30:
            icon, level = "✅", "Low Risk"
        elif risk < 60:
            icon, level = "⚠️", "Moderate Risk"
        else:
            icon, level = "🚨", "High Risk"
        
        st.markdown(f"## {icon} {level}: **{risk:.1f}%**")
        st.progress(int(risk))
        
        # Contributing factors
        st.markdown("### Contributing Factors")
        factors = []
        if age > 55: factors.append(f"• Age {age} (higher risk after 55)")
        if bmi > 30: factors.append(f"• BMI {bmi:.1f} (obese range)")
        elif bmi > 25: factors.append(f"• BMI {bmi:.1f} (overweight range)")
        if ap_hi >= 140 or ap_lo >= 90: factors.append(f"• BP {ap_hi}/{ap_lo} (hypertension)")
        if cholesterol >= 2: factors.append("• Elevated cholesterol")
        if gluc >= 2: factors.append("• Elevated glucose")
        if smoke: factors.append("• Smoker")
        if not active: factors.append("• Sedentary lifestyle")
        
        if factors:
            for f in factors:
                st.markdown(f)
        else:
            st.markdown("• No major risk factors identified 🎉")
        
        st.info("""
        Based on the Kaggle Cardiovascular Disease dataset (70,000 patients).
        Model ROC AUC ≈ 0.80. **Not a substitute for medical advice.**
        """)
    
    # ---------- GENE MODE ----------
    else:
        if gene_data is None:
            st.warning("⚠️ Please upload a gene expression CSV first.")
            st.stop()
        
        for idx in gene_data.index:
            st.subheader(f"Sample: {idx}")
            
            gene_vector = pd.Series(0.0, index=GENE_COLUMNS)
            for gene in GENE_COLUMNS:
                if gene in gene_data.columns:
                    gene_vector[gene] = gene_data.loc[idx, gene]
            clin_vector = pd.Series(0.0, index=CLIN_COLUMNS)
            
            X_input = pd.DataFrame([pd.concat([gene_vector, clin_vector])])
            probs = gene_pipeline.predict_proba(X_input)[0]
            
            st.markdown("**Risk per condition (independent):**")
            for cls, p in zip(encoder.classes_, probs):
                pct = p * 100
                icon = "🟢" if cls == "Healthy" else ("🟡" if cls == "CAD" else "🔴")
                st.markdown(f"{icon} **{cls}**: {pct:.1f}%")
                st.progress(int(pct))
    
    st.markdown("---")
    st.warning("⚠️ **Medical Disclaimer:** Research/education only. Consult a physician.")
