# =============================================================================
# CARDIOVASCULAR RISK AI — STREAMLIT APP (v2)
# Now uses TWO models:
#   1. Gene-expression model (when CSV uploaded)
#   2. Clinical-only model trained on UCI Heart Disease (when no CSV)
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# -----------------------------------------------------------------------
# PAGE CONFIG & STYLING
# -----------------------------------------------------------------------

st.set_page_config(
    page_title="Cardio AI",
    page_icon="❤️",
    layout="wide",
)

# --- Custom CSS for font, background, and layout ---
# --- Custom CSS for font, background, and layout ---
st.markdown("""
<style>
    /* Main background — cerulean blue */
    .stApp {
        background: #007BA7;
    }
    
    /* Fonts — Georgia, white */
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
    
    /* Input labels stay white */
    .stTextInput label, .stNumberInput label, .stSelectbox label, 
    .stRadio label, .stFileUploader label {
        color: white !important;
    }
    
    /* Input boxes — dark text on white background for readability */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        color: #0a1f44 !important;
        background-color: white !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Buttons — dark blue with white text */
    .stButton > button {
        background-color: #0a1f44;
        color: white !important;
        border-radius: 10px;
        border: 2px solid white;
        padding: 0.6rem 2rem;
        font-family: 'Georgia', serif !important;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #1a3a6c;
        transform: translateY(-2px);
    }
    
    /* Sidebar — darker blue */
    section[data-testid="stSidebar"] {
        background: #0a1f44;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Alert boxes (info, warning, error) — keep readable */
    .stAlert {
        color: #0a1f44 !important;
    }
    .stAlert * {
        color: #0a1f44 !important;
    }
    
    /* Tables & dataframes */
    .stDataFrame {
        color: #0a1f44 !important;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #0a1f44 !important;
    }
    
    /* Radio button text */
    .stRadio > div {
        color: white !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: white !important;
        font-family: 'Georgia', serif !important;
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
**clinical data alone** (validated) or **gene expression + clinical data** (research).
""")

if not model_loaded:
    st.error(f"❌ Could not load model files. Error: {load_error}")
    st.stop()

# -----------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------

with st.sidebar:
    st.header("ℹ️ About This Tool")
    st.markdown("""
    **Two prediction modes:**
    
    🩺 **Clinical Mode**  
    Uses standard risk factors (age, BP, cholesterol, etc.) trained on 
    the UCI Heart Disease dataset (Cleveland Clinic).
    
    🧬 **Gene + Clinical Mode**  
    Uses blood gene expression profiles combined with clinical data, 
    trained on NCBI GEO datasets.
    
    ---
    
    **⚠️ Medical Disclaimer**  
    Research tool only. Not a diagnostic device. 
    Consult a physician for medical advice.
    """)

# -----------------------------------------------------------------------
# INPUT MODE
# -----------------------------------------------------------------------

st.header("📋 Patient Information")

input_mode = st.radio(
    "Prediction mode:",
    ["🩺 Clinical only (recommended)", "🧬 Gene expression + clinical"],
    horizontal=True,
)

use_gene_mode = "Gene" in input_mode

# -----------------------------------------------------------------------
# CLINICAL INPUTS (UCI Heart Disease format)
# -----------------------------------------------------------------------

st.subheader("Clinical & Lifestyle Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Demographics**")
    age = st.number_input("Age (years)", 20, 100, 50)
    sex_label = st.selectbox("Sex", ["Female", "Male"])
    sex = 1 if sex_label == "Male" else 0

with col2:
    st.markdown("**Vitals & Labs**")
    trestbps = st.number_input("Resting BP (mmHg)", 80, 220, 130)
    chol = st.number_input("Cholesterol (mg/dL)", 100, 600, 220)
    fbs = 1 if st.selectbox("Fasting Blood Sugar > 120 mg/dL?", ["No", "Yes"]) == "Yes" else 0
    thalach = st.number_input("Max Heart Rate", 60, 220, 150)

with col3:
    st.markdown("**Symptoms & History**")
    cp = st.selectbox("Chest Pain Type", 
                      ["Typical Angina (1)", "Atypical Angina (2)", 
                       "Non-Anginal (3)", "Asymptomatic (4)"])
    cp = int(cp.split("(")[1][0])
    
    exang = 1 if st.selectbox("Exercise-Induced Angina?", ["No", "Yes"]) == "Yes" else 0
    oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, step=0.1)
    
    restecg = st.selectbox("Resting ECG", 
                           ["Normal (0)", "ST-T Abnormality (1)", "LV Hypertrophy (2)"])
    restecg = int(restecg.split("(")[1][0])

# Advanced fields (collapsed)
with st.expander("🔧 Advanced clinical fields (optional)"):
    slope = st.selectbox("ST Slope", ["Upsloping (1)", "Flat (2)", "Downsloping (3)"])
    slope = int(slope.split("(")[1][0])
    ca = st.number_input("Major Vessels Colored (0-3)", 0, 3, 0)
    thal = st.selectbox("Thalassemia", ["Normal (3)", "Fixed Defect (6)", "Reversible Defect (7)"])
    thal = int(thal.split("(")[1][0])

# -----------------------------------------------------------------------
# GENE UPLOAD (only if gene mode)
# -----------------------------------------------------------------------

gene_data = None
if use_gene_mode:
    st.subheader("🧬 Gene Expression Upload")
    uploaded_file = st.file_uploader("Upload gene expression CSV", type=["csv"])
    if uploaded_file:
        gene_data = pd.read_csv(uploaded_file, index_col=0)
        st.success(f"Loaded {gene_data.shape[0]} samples, {gene_data.shape[1]} genes")

# -----------------------------------------------------------------------
# PREDICT
# -----------------------------------------------------------------------

st.markdown("---")

if st.button("🔍 Predict Cardiovascular Risk", type="primary", use_container_width=True):
    
    st.header("📊 Results")
    
    if use_gene_mode and gene_data is None:
        st.warning("Please upload a gene expression CSV or switch to Clinical mode.")
        st.stop()
    
    # ---------- CLINICAL-ONLY MODE ----------
    if not use_gene_mode:
        # Build feature vector matching UCI format
        clin_input = pd.DataFrame([{
            "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
            "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
            "exang": exang, "oldpeak": oldpeak, "slope": slope,
            "ca": ca, "thal": thal,
        }])[CLINICAL_FEATURES]
        
        prob = clinical_model.predict_proba(clin_input)[0]
        heart_disease_risk = prob[1] * 100
        
        # Display
        st.markdown(f"### 🩺 Overall Heart Disease Risk")
        
        if heart_disease_risk < 30:
            color, icon, level = "🟢", "✅", "Low Risk"
        elif heart_disease_risk < 60:
            color, icon, level = "🟡", "⚠️", "Moderate Risk"
        else:
            color, icon, level = "🔴", "🚨", "High Risk"
        
        st.markdown(f"## {icon} {level}: **{heart_disease_risk:.1f}%**")
        st.progress(int(heart_disease_risk))
        
        st.info(f"""
        This estimate is based on the UCI Heart Disease dataset (n=297 patients).
        Model AUC ≈ 0.90 on held-out test data.
        
        **Not a substitute for professional medical assessment.**
        """)
    
    # ---------- GENE + CLINICAL MODE ----------
    else:
        for idx in gene_data.index:
            st.subheader(f"Sample: {idx}")
            
            # Build gene vector (0 for missing genes)
            gene_vector = pd.Series(0.0, index=GENE_COLUMNS)
            for gene in GENE_COLUMNS:
                if gene in gene_data.columns:
                    gene_vector[gene] = gene_data.loc[idx, gene]
            
            # Clinical vector (empty for gene model since GEO didn't have clinical)
            clin_vector = pd.Series(0.0, index=CLIN_COLUMNS)
            
            X_input = pd.DataFrame([pd.concat([gene_vector, clin_vector])])
            probs = gene_pipeline.predict_proba(X_input)[0]
            
            # Independent risk display (NOT summing to 100%)
            st.markdown("**Risk per condition (independent):**")
            for cls, p in zip(encoder.classes_, probs):
                pct = p * 100
                if cls == "Healthy":
                    st.markdown(f"🟢 **{cls}**: {pct:.1f}%")
                elif cls == "CAD":
                    st.markdown(f"🟡 **{cls}**: {pct:.1f}%")
                else:
                    st.markdown(f"🔴 **{cls}**: {pct:.1f}%")
                st.progress(int(pct))
    
    st.markdown("---")
    st.warning("⚠️ **Medical Disclaimer:** For research/education only. Consult a physician.")
