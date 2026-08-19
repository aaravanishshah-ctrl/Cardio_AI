# =============================================================================
# CARDIOVASCULAR RISK AI — STREAMLIT APP (v5)
# - Fixed upload button overlap (properly hides Material Icons)
# - Fixed sidebar toggle button visibility
# - Added new "About the Diseases" educational tab
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
    
    /* Main predict button — white bg, dark navy text */
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
    
    /* --- HIDE ALL MATERIAL ICON TEXT (fixes "keyboard_double" & "upload" overlap) --- */
    span.material-icons,
    span.material-icons-outlined,
    span.material-symbols-outlined,
    span.material-symbols-rounded,
    [class*="material-symbols"],
    [class*="material-icons"] {
        font-family: 'Material Symbols Rounded', 'Material Icons' !important;
        font-size: 1.2rem !important;
        color: #0a1f44 !important;
        line-height: 1 !important;
    }
    
    /* Sidebar toggle button (top-left arrow) — make visible */
    [data-testid="stSidebarCollapsedControl"] {
        background-color: white !important;
        border-radius: 8px !important;
        padding: 6px !important;
        border: 2px solid #0a1f44 !important;
    }
    [data-testid="stSidebarCollapsedControl"] * {
        color: #0a1f44 !important;
    }
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: #0a1f44 !important;
        color: #0a1f44 !important;
        width: 20px !important;
        height: 20px !important;
    }
    /* Hide any accidental Material text in header buttons */
    header [class*="material"],
    [data-testid="stSidebarCollapsedControl"] span:not(:has(svg)) {
        display: none !important;
    }
    
    /* Sidebar itself */
    section[data-testid="stSidebar"] {
        background: #0a1f44;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Sidebar close button */
    [data-testid="stSidebar"] button svg {
        fill: white !important;
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
    
    /* --- FILE UPLOADER FIX v2 --- */
    /* Label above the uploader — WHITE */
    .stFileUploader > label,
    .stFileUploader label,
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] > label,
    [data-testid="stFileUploader"] label p {
        color: white !important;
        font-family: 'Georgia', serif !important;
        font-weight: 600;
    }
    
    /* Drop zone background — white */
    [data-testid="stFileUploaderDropzone"] {
        background-color: white !important;
        border-radius: 8px;
    }
    
    /* Text inside drop zone — dark */
    [data-testid="stFileUploaderDropzone"] * {
        color: #0a1f44 !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* "Browse files" button — fix overlap */
    [data-testid="stFileUploaderDropzone"] button {
        background-color: white !important;
        color: #0a1f44 !important;
        border: 2px solid #0a1f44 !important;
        border-radius: 8px !important;
        padding: 0.4rem 1.2rem !important;
        font-family: 'Georgia', serif !important;
        font-weight: 600 !important;
        min-width: 130px !important;
        white-space: nowrap !important;
    }
    
    /* Hide the raw material-icon TEXT that says "upload" */
    [data-testid="stFileUploaderDropzone"] button span.material-icons,
    [data-testid="stFileUploaderDropzone"] button span[class*="material"],
    [data-testid="stFileUploaderDropzone"] button [class*="icon"] {
        display: none !important;
    }
    
    [data-testid="stFileUploaderDropzone"] button p {
        color: #0a1f44 !important;
        margin: 0 !important;
        padding: 0 !important;
        font-family: 'Georgia', serif !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(255,255,255,0.15);
        border-radius: 10px;
        padding: 0.4rem;
        gap: 0.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: white !important;
        font-family: 'Georgia', serif !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: white !important;
        color: #0a1f44 !important;
    }
    .stTabs [aria-selected="true"] * {
        color: #0a1f44 !important;
    }
    
    /* Citations box */
    .citation-box {
        background-color: rgba(255,255,255,0.1);
        border-left: 4px solid white;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
        border-radius: 6px;
        font-size: 0.9rem;
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
**clinical/lifestyle data** or **gene expression profiles**.
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
    Predicts cardiovascular disease risk from lifestyle 
    and clinical factors. Trained on 70,000 patients 
    (Kaggle Cardiovascular Disease dataset).
    
    🧬 **Gene Expression Mode**  
    Classifies blood samples as CAD, Heart Failure, or 
    Healthy using gene expression profiles from NCBI GEO.
    
    ---
    
    **⚠️ Disclaimer**  
    Research/educational tool. Not a diagnostic device.
    """)

# -----------------------------------------------------------------------
# TABS
# -----------------------------------------------------------------------

tab1, tab2 = st.tabs(["🔍 Risk Prediction", "📚 Learn About the Diseases"])

# =======================================================================
# TAB 1 — RISK PREDICTION
# =======================================================================

with tab1:
    st.header("📋 Choose Input Mode")
    
    input_mode = st.radio(
        "Prediction mode:",
        ["🩺 Clinical / Lifestyle (recommended)", "🧬 Gene Expression"],
        horizontal=True,
    )
    
    use_gene_mode = "Gene" in input_mode
    st.markdown("---")
    
    # ------- CLINICAL MODE INPUTS -------
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
    
    # ------- GENE MODE INPUTS -------
    else:
        st.subheader("🧬 Gene Expression Upload")
        st.markdown("""
        Upload a **CSV file** where:
        - Each **row** is one sample (patient)
        - Each **column** is a gene symbol (e.g. `TP53`, `IL6`, `BRCA1`)
        - Values should be normalized expression (log2 or z-score)
        """)
        
        uploaded_file = st.file_uploader("Upload gene expression CSV", type=["csv"])
        gene_data = None
        if uploaded_file:
            gene_data = pd.read_csv(uploaded_file, index_col=0)
            st.success(f"✅ Loaded {gene_data.shape[0]} sample(s), {gene_data.shape[1]} genes")
            with st.expander("Preview data"):
                st.dataframe(gene_data.head(3))
    
    st.markdown("---")
    
    # ------- PREDICT BUTTON -------
    if st.button("🔍 Predict Cardiovascular Risk", type="primary", use_container_width=True):
        st.header("📊 Results")
        
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
                icon, level = "✅", "Low Risk"
            elif risk < 60:
                icon, level = "⚠️", "Moderate Risk"
            else:
                icon, level = "🚨", "High Risk"
            
            st.markdown(f"## {icon} {level}: **{risk:.1f}%**")
            st.progress(int(risk))
            
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

# =======================================================================
# TAB 2 — EDUCATIONAL CONTENT
# =======================================================================

with tab2:
    st.header("📚 Understanding Cardiovascular Diseases")
    st.markdown("""
    Cardiovascular diseases (CVDs) are the **leading cause of death worldwide**, 
    responsible for an estimated 17.9 million deaths each year, according to the 
    World Health Organization [1]. This tool focuses on three key outcomes: 
    **Coronary Artery Disease (CAD)**, **Heart Failure (HF)**, and general 
    **Cardiovascular Risk**. Below is an overview of each condition, its risk 
    factors, and why early identification matters.
    """)
    
    st.subheader("🫀 Coronary Artery Disease (CAD)")
    st.markdown("""
    Coronary Artery Disease is caused by the buildup of atherosclerotic plaque — 
    deposits of cholesterol, fat, calcium, and inflammatory cells — inside the 
    coronary arteries that supply blood to the heart muscle. Over time, these 
    plaques narrow the artery walls, reducing oxygen delivery and potentially 
    leading to angina (chest pain), myocardial infarction (heart attack), or 
    sudden cardiac death [2]. CAD is often silent for decades before symptoms 
    appear, making early risk assessment critical. Major risk factors include 
    hypertension, high LDL cholesterol, smoking, diabetes, obesity, family 
    history, and physical inactivity [3].
    
    Research using **blood-based gene expression profiling** has identified 
    inflammatory and immune-cell transcriptional signatures that distinguish 
    CAD patients from healthy controls, even before overt symptoms develop. 
    Studies such as those by Elashoff et al. [4] and Sinnaeve et al. [5] have 
    demonstrated that peripheral whole-blood RNA expression can serve as a 
    non-invasive biomarker for obstructive CAD.
    """)
    
    st.subheader("💔 Heart Failure (HF)")
    st.markdown("""
    Heart Failure is a chronic, progressive condition in which the heart cannot 
    pump enough blood to meet the body's needs. It affects over 64 million 
    people globally [6]. HF is not a single disease but a clinical syndrome 
    resulting from structural or functional cardiac abnormalities — commonly 
    following a myocardial infarction, chronic hypertension, or valvular 
    disease. Symptoms include shortness of breath, fatigue, swelling in the 
    legs, and reduced exercise tolerance [7].
    
    A key research focus is identifying patients at risk of developing HF 
    **after** a heart attack. The GSE59867 dataset, used in this tool's gene 
    expression model, tracks post-STEMI patients across four timepoints and 
    identifies transcriptomic signatures that predict which patients will 
    progress to HF versus recover normally [8]. Early identification enables 
    earlier interventions such as beta-blockers, ACE inhibitors, or SGLT2 
    inhibitors, which have been shown to reduce HF-related mortality [9].
    """)
    
    st.subheader("🩺 General Cardiovascular Risk & Prevention")
    st.markdown("""
    Beyond specific diseases, overall cardiovascular risk reflects the 
    likelihood of experiencing any major adverse cardiac event (heart attack, 
    stroke, or cardiac death) within a defined period, typically 10 years. 
    Established risk calculators such as the **ASCVD Risk Estimator** (from 
    the American Heart Association) and the **Framingham Risk Score** use 
    variables like age, sex, blood pressure, cholesterol, smoking status, and 
    diabetes to stratify patients into low, moderate, or high-risk categories 
    [10]. This tool's clinical model is trained on the Kaggle Cardiovascular 
    Disease dataset (70,000 patients), which uses a similar set of preventive 
    features.
    
    Prevention remains the most powerful intervention. The INTERHEART study 
    [11] found that **nine modifiable risk factors** — smoking, abnormal lipids, 
    hypertension, diabetes, abdominal obesity, psychosocial stress, low fruit 
    and vegetable intake, alcohol consumption, and physical inactivity — 
    account for over **90% of the population-attributable risk of a first 
    myocardial infarction** worldwide. Even modest lifestyle improvements 
    (30 minutes of daily activity, quitting smoking, Mediterranean-style diet) 
    substantially reduce risk.
    """)
    
    st.subheader("🧬 The Role of AI and Gene Expression")
    st.markdown("""
    Machine learning models like the one powering this tool combine 
    high-dimensional biological data (gene expression from thousands of genes) 
    with clinical measurements to detect patterns invisible to traditional 
    statistical methods. Studies have shown that AI-based risk stratification 
    can outperform conventional risk scores in specific populations [12], 
    particularly when integrating multi-omic and lifestyle data. However, 
    these tools are not diagnostic — they are **decision-support aids** meant 
    to complement, not replace, clinical judgment. Ongoing challenges include 
    dataset diversity (most training data comes from European and North 
    American populations), interpretability, and rigorous prospective 
    validation before clinical deployment [13].
    """)
    
    st.markdown("---")
    
    st.subheader("📖 Works Cited")
    st.markdown("""
    <div class="citation-box">
    [1] World Health Organization. (2021). <i>Cardiovascular diseases (CVDs)</i>. 
    https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
    
    [2] Libby, P., et al. (2019). Atherosclerosis. <i>Nature Reviews Disease 
    Primers</i>, 5(1), 56.
    
    [3] Arnett, D. K., et al. (2019). 2019 ACC/AHA Guideline on the Primary 
    Prevention of Cardiovascular Disease. <i>Circulation</i>, 140(11), e596–e646.
    
    [4] Elashoff, M. R., et al. (2011). Development of a blood-based gene 
    expression algorithm for assessment of obstructive coronary artery disease 
    in non-diabetic patients. <i>BMC Medical Genomics</i>, 4, 26.
    
    [5] Sinnaeve, P. R., et al. (2009). Gene expression patterns in peripheral 
    blood correlate with the extent of coronary artery disease. 
    <i>PLoS ONE</i>, 4(9), e7037.
    
    [6] Groenewegen, A., et al. (2020). Epidemiology of heart failure. 
    <i>European Journal of Heart Failure</i>, 22(8), 1342–1356.
    
    [7] McDonagh, T. A., et al. (2021). 2021 ESC Guidelines for the diagnosis 
    and treatment of acute and chronic heart failure. <i>European Heart 
    Journal</i>, 42(36), 3599–3726.
    
    [8] Maciejak, A., et al. (2015). Gene expression profiling reveals 
    potential prognostic biomarkers associated with the progression of heart 
    failure. <i>Genome Medicine</i>, 7, 26. (Dataset: GSE59867, NCBI GEO.)
    
    [9] Zannad, F., et al. (2020). SGLT2 inhibitors in patients with heart 
    failure with reduced ejection fraction. <i>The Lancet</i>, 396(10254), 
    819–829.
    
    [10] Goff, D. C., et al. (2014). 2013 ACC/AHA guideline on the assessment 
    of cardiovascular risk. <i>Circulation</i>, 129(25 suppl 2), S49–S73.
    
    [11] Yusuf, S., et al. (2004). Effect of potentially modifiable risk 
    factors associated with myocardial infarction in 52 countries (the 
    INTERHEART study). <i>The Lancet</i>, 364(9438), 937–952.
    
    [12] Weng, S. F., et al. (2017). Can machine-learning improve 
    cardiovascular risk prediction using routine clinical data? 
    <i>PLoS ONE</i>, 12(4), e0174944.
    
    [13] Krittanawong, C., et al. (2020). Machine learning prediction in 
    cardiovascular diseases: a meta-analysis. <i>Scientific Reports</i>, 
    10, 16057.
    </div>
    """, unsafe_allow_html=True)
