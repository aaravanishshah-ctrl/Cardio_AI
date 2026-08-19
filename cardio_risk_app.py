# =============================================================================
# CARDIOVASCULAR RISK AI — STREAMLIT APP
# cardio_risk_app.py
#
# How to run locally:
#   streamlit run cardio_risk_app.py
#
# How to deploy to Streamlit Cloud:
#   1. Push this file + the 4 .pkl files to a GitHub repo
#   2. Go to share.streamlit.io and connect your repo
#   3. Set the main file path to cardio_risk_app.py
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# -----------------------------------------------------------------------
# 0. PAGE CONFIG
# -----------------------------------------------------------------------

st.set_page_config(
    page_title="Cardiovascular Risk AI",
    page_icon="❤️",
    layout="wide",
)

# -----------------------------------------------------------------------
# 1. LOAD MODEL FILES
# -----------------------------------------------------------------------

@st.cache_resource
def load_model():
    """Load the trained pipeline and supporting files.
    Looks in the same directory as this script."""
    base = os.path.dirname(os.path.abspath(__file__))
    pipeline  = joblib.load(os.path.join(base, "cardio_pipeline.pkl"))
    encoder   = joblib.load(os.path.join(base, "label_encoder.pkl"))
    gene_cols = joblib.load(os.path.join(base, "gene_columns.pkl"))
    clin_cols = joblib.load(os.path.join(base, "clinical_columns.pkl"))
    return pipeline, encoder, gene_cols, clin_cols

try:
    full_pipeline, encoder, GENE_COLUMNS, CLIN_COLUMNS = load_model()
    model_loaded = True
except FileNotFoundError as e:
    model_loaded = False
    load_error = str(e)

# -----------------------------------------------------------------------
# 2. HEADER
# -----------------------------------------------------------------------

st.title("❤️ Cardiovascular Risk AI")
st.markdown("""
This tool uses a machine-learning model trained on real blood-based gene 
expression data from NCBI GEO to estimate cardiovascular risk across three 
categories:

| Category | Description |
|---|---|
| **CAD** | Coronary Artery Disease |
| **Heart Failure** | Post-MI / heart-failure gene signature |
| **Healthy** | No significant cardiovascular disease signal |

> ⚠️ **This is a research tool only. It is not a medical diagnostic device. 
> Always consult a qualified physician.**
""")

if not model_loaded:
    st.error(f"""
    ❌ Could not load model files. Make sure these 4 files are in the 
    same folder as cardio_risk_app.py:
    - cardio_pipeline.pkl
    - label_encoder.pkl
    - gene_columns.pkl
    - clinical_columns.pkl
    
    Error: {load_error}
    """)
    st.stop()

st.success("✅ Model loaded successfully.")

# -----------------------------------------------------------------------
# 3. SIDEBAR — HOW IT WORKS
# -----------------------------------------------------------------------

with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    **Input options:**
    
    1. **Clinical only** — Enter age, sex, BMI, blood pressure, 
    cholesterol, lifestyle factors. The model will use these features 
    alone (gene columns will be filled with zeros).
    
    2. **Gene expression + clinical** — If you have a blood gene 
    expression profile (e.g. from a microarray or RNA-seq experiment), 
    upload it as a CSV. Clinical features are still used alongside it.
    
    **Model details:**
    - Algorithm: XGBoost (multiclass softprob)
    - Training data: GSE20680, GSE20681 (CAD); GSE59867 (Heart Failure)
    - Features: ~16,000 gene expression features + clinical metadata
    - Gene selection: Top 500 by ANOVA F-score (SelectKBest)
    
    **Output:**
    - Risk probability (%) for each class
    - Most likely condition
    """)
    
    st.header("📁 Model files")
    st.markdown("""
    Files loaded:
    - `cardio_pipeline.pkl`
    - `label_encoder.pkl`
    - `gene_columns.pkl`
    - `clinical_columns.pkl`
    """)

# -----------------------------------------------------------------------
# 4. INPUT MODE SELECTION
# -----------------------------------------------------------------------

st.header("📋 Patient Input")

input_mode = st.radio(
    "Choose input mode:",
    ["Clinical features only", "Gene expression CSV + clinical features"],
    horizontal=True,
)

# -----------------------------------------------------------------------
# 5. CLINICAL FEATURE INPUTS
# -----------------------------------------------------------------------

st.subheader("🩺 Clinical & Lifestyle Features")
st.markdown("Fill in as many fields as you know. Leave unknown fields blank.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Demographics**")
    age = st.number_input("Age (years)", min_value=0, max_value=120, 
                           value=None, placeholder="e.g. 55")
    sex = st.selectbox("Sex", ["", "Male", "Female", "Other"])
    bmi = st.number_input("BMI (kg/m²)", min_value=0.0, max_value=80.0, 
                           value=None, placeholder="e.g. 27.5")

with col2:
    st.markdown("**Blood Pressure & Labs**")
    sbp = st.number_input("Systolic BP (mmHg)", min_value=0, max_value=300, 
                           value=None, placeholder="e.g. 130")
    dbp = st.number_input("Diastolic BP (mmHg)", min_value=0, max_value=200, 
                           value=None, placeholder="e.g. 85")
    total_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=0.0, 
                                  max_value=1000.0, value=None, 
                                  placeholder="e.g. 210")
    ldl = st.number_input("LDL (mg/dL)", min_value=0.0, max_value=1000.0, 
                           value=None, placeholder="e.g. 130")
    hdl = st.number_input("HDL (mg/dL)", min_value=0.0, max_value=500.0, 
                           value=None, placeholder="e.g. 45")
    trig = st.number_input("Triglycerides (mg/dL)", min_value=0.0, 
                            max_value=5000.0, value=None, 
                            placeholder="e.g. 150")

with col3:
    st.markdown("**Lifestyle & History**")
    smoking = st.selectbox("Smoking Status", 
                            ["", "Never", "Former", "Current"])
    diabetes = st.selectbox("Diabetes", ["", "No", "Yes"])
    hypertension = st.selectbox("Hypertension", ["", "No", "Yes"])
    family_hx = st.selectbox("Family History of Heart Disease", 
                               ["", "No", "Yes"])

# -----------------------------------------------------------------------
# 6. GENE EXPRESSION UPLOAD (optional)
# -----------------------------------------------------------------------

gene_data = None

if input_mode == "Gene expression CSV + clinical features":
    st.subheader("🧬 Gene Expression Upload")
    st.markdown("""
    Upload a **CSV file** where:
    - Each **row** is one sample (or just one row for a single patient)
    - Each **column** is a gene symbol (e.g. `TP53`, `BRCA1`, `IL6`)
    - Values should be **normalized expression values** (log2 or similar)
    
    Genes not in the training set will be ignored. Missing training genes 
    will be filled with `0` (mean after z-scoring).
    """)
    
    uploaded_file = st.file_uploader(
        "Upload gene expression CSV", type=["csv"]
    )
    
    if uploaded_file is not None:
        try:
            gene_data = pd.read_csv(uploaded_file, index_col=0)
            st.success(f"✅ Loaded {gene_data.shape[0]} sample(s), "
                       f"{gene_data.shape[1]} genes.")
            st.dataframe(gene_data.head(3))
        except Exception as e:
            st.error(f"❌ Could not read CSV: {e}")
            gene_data = None

# -----------------------------------------------------------------------
# 7. BUILD FEATURE VECTOR
# -----------------------------------------------------------------------

def build_feature_vector(gene_data_row=None):
    """
    Build one-row DataFrame with GENE_COLUMNS + CLIN_COLUMNS.
    Gene columns not present in the upload are filled with 0.
    Clinical columns are filled from the sidebar inputs.
    """
    # --- Gene features
    gene_vector = pd.Series(0.0, index=GENE_COLUMNS)
    if gene_data_row is not None:
        for gene in GENE_COLUMNS:
            if gene in gene_data_row.index:
                gene_vector[gene] = gene_data_row[gene]

    # --- Clinical features
    # Build the same structure as training:
    # numeric fields first, then one-hot dummies for categoricals
    clin_vector = pd.Series(np.nan, index=CLIN_COLUMNS)

    # Map numeric inputs to the column names used during training
    numeric_map = {
        "age": age,
        "bmi": bmi,
        "systolic bp": sbp,
        "diastolic bp": dbp,
        "total cholesterol": total_chol,
        "ldl": ldl,
        "hdl": hdl,
        "triglycerides": trig,
    }
    for col, val in numeric_map.items():
        if col in clin_vector.index and val is not None:
            clin_vector[col] = float(val)

    # Map categorical one-hot columns
    # Training used pd.get_dummies with prefix=col, e.g. "sex_Male"
    categorical_map = {
        "sex": sex,
        "gender": sex,
        "smoking status": smoking,
        "diabetes": diabetes,
        "hypertension": hypertension,
        "family history": family_hx,
    }
    for col, val in categorical_map.items():
        if val:  # only if user selected something
            dummy_col = f"{col}_{val}"
            if dummy_col in clin_vector.index:
                clin_vector[dummy_col] = 1.0
            # Set all other dummies for this prefix to 0
            for c in clin_vector.index:
                if c.startswith(f"{col}_") and c != dummy_col:
                    if pd.isna(clin_vector[c]):
                        clin_vector[c] = 0.0

    # Combine into one row
    full_vector = pd.concat([gene_vector, clin_vector])
    return pd.DataFrame([full_vector])

# -----------------------------------------------------------------------
# 8. PREDICT
# -----------------------------------------------------------------------

st.markdown("---")

predict_button = st.button("🔍 Predict Cardiovascular Risk", 
                            type="primary", use_container_width=True)

if predict_button:
    
    # Figure out which samples to predict
    if input_mode == "Gene expression CSV + clinical features":
        if gene_data is None:
            st.warning("⚠️ Please upload a gene expression CSV first, "
                       "or switch to clinical-only mode.")
            st.stop()
        samples_to_predict = [
            (idx, gene_data.loc[idx]) for idx in gene_data.index
        ]
    else:
        samples_to_predict = [("Patient", None)]

    st.header("📊 Results")

    for sample_name, gene_row in samples_to_predict:
        
        st.subheader(f"Sample: {sample_name}")
        
        try:
            X_input = build_feature_vector(gene_data_row=gene_row)
            probs = full_pipeline.predict_proba(X_input)[0]
            results = {
                cls: round(float(p) * 100, 2)
                for cls, p in zip(encoder.classes_, probs)
            }
            results_sorted = dict(
                sorted(results.items(), key=lambda x: x[1], reverse=True)
            )

            # Top prediction
            top_condition = list(results_sorted.keys())[0]
            top_prob = list(results_sorted.values())[0]

            # Color coding
            if top_condition == "Healthy":
                color = "green"
                icon = "✅"
            elif top_condition == "CAD":
                color = "orange"
                icon = "⚠️"
            else:
                color = "red"
                icon = "🚨"

            st.markdown(
                f"### {icon} Most likely: "
                f"**:{color}[{top_condition}]** "
                f"({top_prob:.1f}% probability)"
            )

            # Probability bars for all classes
            st.markdown("**Risk breakdown:**")
            for condition, prob in results_sorted.items():
                if condition == "Healthy":
                    bar_color = "green"
                elif condition == "CAD":
                    bar_color = "orange"
                else:
                    bar_color = "red"
                
                st.markdown(f"**{condition}**")
                st.progress(int(prob))
                st.markdown(f"{prob:.1f}%")

            # Results table
            results_df = pd.DataFrame(
                list(results_sorted.items()),
                columns=["Condition", "Risk (%)"]
            )
            st.dataframe(results_df, use_container_width=True)

        except Exception as e:
            st.error(f"❌ Prediction failed for {sample_name}: {e}")

    # Disclaimer
    st.markdown("---")
    st.warning("""
    ⚠️ **Medical Disclaimer:** This tool is for research and educational 
    purposes only. It is not validated for clinical use and should not be 
    used to make medical decisions. Always consult a qualified healthcare 
    professional for medical advice, diagnosis, or treatment.
    """)
