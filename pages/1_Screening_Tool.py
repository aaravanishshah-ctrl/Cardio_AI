# =============================================================================
# CardioAI — SCREENING TOOL PAGE (Clinical Light Theme)
# All inputs use quantitative clinical values & exact number inputs.
# =============================================================================

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from styles import apply_styles, render_footer, render_navbar

st.set_page_config(
    page_title="Screening Tool — CardioAI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()
render_navbar(active_page="screening")


# -----------------------------------------------------------------------
# LOAD MODELS
# -----------------------------------------------------------------------
@st.cache_resource
def load_models():
  base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  gene_pipeline = joblib.load(os.path.join(base, "cardio_pipeline.pkl"))
  encoder = joblib.load(os.path.join(base, "label_encoder.pkl"))
  gene_cols = joblib.load(os.path.join(base, "gene_columns.pkl"))
  clin_cols = joblib.load(os.path.join(base, "clinical_columns.pkl"))
  clinical_model = joblib.load(os.path.join(base, "clinical_only_model.pkl"))
  clinical_features = joblib.load(
      os.path.join(base, "clinical_feature_names.pkl")
  )
  return (
      gene_pipeline,
      encoder,
      gene_cols,
      clin_cols,
      clinical_model,
      clinical_features,
  )


try:
  (
      gene_pipeline,
      encoder,
      GENE_COLUMNS,
      CLIN_COLUMNS,
      clinical_model,
      CLINICAL_FEATURES,
  ) = load_models()
except FileNotFoundError as e:
  st.error(f"Could not load model files: {e}")
  st.stop()


# -----------------------------------------------------------------------
# CLINICAL CONVERSION HELPERS
# -----------------------------------------------------------------------
def chol_to_cat(mgdl):
  if mgdl < 200:
    return 1  # Desirable (<200 mg/dL)
  if mgdl < 240:
    return 2  # Borderline High (200-239 mg/dL)
  return 3  # High Risk (≥240 mg/dL)


def gluc_to_cat(mgdl):
  if mgdl < 100:
    return 1  # Normal (<100 mg/dL)
  if mgdl < 126:
    return 2  # Prediabetes (100-125 mg/dL)
  return 3  # Diabetes (≥126 mg/dL)


def htn_staging(sys, dia):
  if sys < 120 and dia < 80:
    return 5, "Normal BP (<120/<80 mmHg)"
  if sys < 130 and dia < 80:
    return 25, "Elevated BP (120-129/<80 mmHg)"
  if (130 <= sys < 140) or (80 <= dia < 90):
    return 55, "Stage 1 Hypertension (130-139/80-89 mmHg)"
  if sys >= 140 or dia >= 90:
    if sys >= 180 or dia >= 120:
      return 95, "Hypertensive Crisis (≥180/≥120 mmHg)"
    return 80, "Stage 2 Hypertension (≥140/≥90 mmHg)"
  return 10, "Normal BP"


def met_syndrome_score(bmi, sys, dia, gluc, chol):
  criteria = 0
  if bmi >= 30:
    criteria += 1
  if sys >= 130 or dia >= 85:
    criteria += 1
  if gluc >= 100:
    criteria += 1
  if chol >= 200:
    criteria += 1
  pct = min(100, criteria * 25)
  if criteria >= 3:
    label = "High Risk — Meets Metabolic Syndrome Threshold"
  elif criteria == 2:
    label = "Moderate Risk — 2 Risk Factors Present"
  else:
    label = "Low Risk"
  return pct, label, criteria


def cad_risk_calc(age, gender, chol, sys, cigs, bmi):
  score = 0
  if age >= 45 and gender == 2:
    score += 15
  if age >= 55 and gender == 1:
    score += 15
  if chol >= 240:
    score += 20
  elif chol >= 200:
    score += 10
  if sys >= 140:
    score += 15
  if cigs > 0:
    score += 20
  if bmi >= 30:
    score += 10
  return min(100, score)


def stroke_risk_calc(age, sys, cigs, gluc):
  score = 0
  if age >= 55:
    score += 20
  if age >= 65:
    score += 15
  if sys >= 140:
    score += 25
  if sys >= 160:
    score += 15
  if cigs > 0:
    score += 15
  if gluc >= 126:
    score += 10
  return min(100, score)


# -----------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------
st.markdown(
    """
<div style="padding: 1.5rem 0 1rem 0;">
    <div class="section-label">Screening Tool</div>
    <h1 class="hero-title" style="font-size: 2.75rem;">Begin <span class="hero-title-accent" style="color: #1e40af;">assessment.</span></h1>
    <p class="hero-subtitle">
        Enter exact quantitative clinical values below or upload blood transcriptomic profiles.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

input_mode = st.radio(
    "",
    ["Clinical / Lifestyle", "Gene Expression"],
    horizontal=True,
    label_visibility="collapsed",
)
use_gene_mode = "Gene" in input_mode

st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)

# =======================================================================
# CLINICAL MODE
# =======================================================================
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
    st.markdown(
        "<div style='color:#1e40af; font-weight:600; margin-top:0.5rem;'>BMI:"
        f" {bmi:.1f}</div>",
        unsafe_allow_html=True,
    )

  with col2:
    st.markdown("**Vitals & Lab Values**")
    ap_hi = st.number_input("Systolic BP (mmHg)", 70, 250, 120)
    ap_lo = st.number_input("Diastolic BP (mmHg)", 40, 200, 80)
    chol_mgdl = st.number_input("Total Cholesterol (mg/dL)", 100, 500, 180)
    gluc_mgdl = st.number_input("Fasting Glucose (mg/dL)", 50, 400, 95)

  with col3:
    st.markdown("**Lifestyle Quantities**")
    cigs_per_day = st.number_input("Cigarettes per day", 0, 60, 0)
    drinks_per_week = st.number_input("Alcoholic drinks / week", 0, 50, 0)
    exercise_min = st.number_input("Exercise (min / week)", 0, 1500, 150)

  # Internal mappings for ML model
  cholesterol = chol_to_cat(chol_mgdl)
  gluc = gluc_to_cat(gluc_mgdl)
  smoke = 1 if cigs_per_day > 0 else 0
  alco = 1 if drinks_per_week >= 7 else 0
  active = 1 if exercise_min >= 150 else 0

# =======================================================================
# GENE MODE
# =======================================================================
else:
  st.markdown("""
    Upload a CSV where each row is a sample and each column is a gene symbol 
    (e.g. TP53, IL6). Values should be normalized (log2 or z-score).
    """)
  uploaded_file = st.file_uploader("Gene expression CSV", type=["csv"])
  gene_data = None
  if uploaded_file:
    gene_data = pd.read_csv(uploaded_file, index_col=0)
    st.success(
        f"Loaded {gene_data.shape[0]} sample(s), {gene_data.shape[1]} genes"
    )

st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)

# =======================================================================
# PREDICT BUTTON & RESULTS
# =======================================================================
if st.button("Begin Assessment →", type="primary"):
  st.markdown("<hr>", unsafe_allow_html=True)
  st.markdown(
      '<div class="section-label">Results</div>', unsafe_allow_html=True
  )

  if not use_gene_mode:
    # 1. Overall CVD Risk via ML
    try:
      pulse_pressure = ap_hi - ap_lo
      map_val = (ap_hi + 2 * ap_lo) / 3
      bp_stage = (
          0
          if (ap_hi < 120 and ap_lo < 80)
          else (
              1
              if ap_hi < 130 and ap_lo < 80
              else (2 if ap_hi < 140 or ap_lo < 90 else 3)
          )
      )
      bmi_cat = (
          0
          if bmi < 18.5
          else (1 if bmi < 25 else (2 if bmi < 30 else 3))
      )
      age_group = (
          0
          if age < 40
          else (
              1
              if age < 50
              else (2 if age < 60 else (3 if age < 70 else 4))
          )
      )
      n_risk = (
          int(cholesterol > 1)
          + int(gluc > 1)
          + int(smoke == 1)
          + int(active == 0)
          + int(bmi >= 30)
          + int(ap_hi >= 140)
          + int(age >= 55)
      )
      female_postmeno = int(gender == 1 and age >= 55)

      full_feats = {
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
          "pulse_pressure": pulse_pressure,
          "map": map_val,
          "bp_stage": bp_stage,
          "bmi_cat": bmi_cat,
          "age_group": age_group,
          "age_x_bmi": age * bmi,
          "age_x_sys": age * ap_hi,
          "bmi_x_chol": bmi * cholesterol,
          "smoke_x_age": smoke * age,
          "active_x_bmi": active * bmi,
          "chol_x_gluc": cholesterol * gluc,
          "pp_x_age": pulse_pressure * age,
          "n_risk_factors": n_risk,
          "female_postmeno": female_postmeno,
          "height": height,
          "weight": weight,
      }
      clin_input = pd.DataFrame([full_feats])[CLINICAL_FEATURES]
    except KeyError:
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
    overall_risk = prob[1] * 100

    if overall_risk < 30:
      overall_level, overall_color = "Low Risk", "#059669"
    elif overall_risk < 60:
      overall_level, overall_color = "Moderate Risk", "#d97706"
    else:
      overall_level, overall_color = "High Risk", "#dc2626"

    # Overall Risk Display
    st.markdown(
        f"""
        <div class="result-card">
            <div style="color: #64748b; font-size: 0.8rem; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 600;">
                Overall Cardiovascular Event Probability (Machine Learning)
            </div>
            <div class="risk-score-huge" style="color: {overall_color};">{overall_risk:.1f}%</div>
            <div style="font-size: 1.25rem; color: {overall_color}; font-weight: 600;">
                {overall_level}
            </div>
            <div style="color: #475569; font-size: 0.85rem; margin-top: 0.8rem; line-height: 1.5;">
                Trained on 70,000 patient records (Kaggle Cardiovascular Cohort). 
                Represents statistical probability of experiencing an adverse cardiovascular event.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(int(overall_risk))

    # Explanatory Banner
    st.markdown(
        """
        <div style="background: #f1f5f9; border: 1px solid #cbd5e1; padding: 0.9rem 1.1rem; border-radius: 6px; margin-top: 2rem; margin-bottom: 1.25rem;">
            <div style="color: #1e40af; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.2rem;">
                💡 Clinical Staging vs. Probability Notice
            </div>
            <div style="color: #475569; font-size: 0.85rem; line-height: 1.5;">
                <b>Overall Risk</b> (above) is a statistical Machine Learning probability.<br>
                <b>Specific Condition Profiles</b> (below) represent <b>AHA/ACC & Framingham Guideline Staging Scores (0–100)</b> to indicate severity and criteria progression, <i>not an immediate probability of an event</i>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Subtype Breakdown
    st.markdown(
        "<h3 style='margin-top: 1.5rem;'>Specific Condition Clinical"
        " Staging</h3>",
        unsafe_allow_html=True,
    )

    htn_pct, htn_label = htn_staging(ap_hi, ap_lo)
    htn_color = (
        "#059669" if htn_pct < 30 else ("#d97706" if htn_pct < 60 else "#dc2626")
    )
    st.markdown(
        f"""
        <div class="result-card" style="padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 1.15rem; color: #0f172a; font-weight: 600;">Hypertension</div>
                    <div style="color: #475569; font-size: 0.85rem; margin-top: 0.25rem;">2017 AHA/ACC Guideline Staging: {htn_label}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2rem; color: {htn_color}; font-weight: 700;">{htn_pct}/100</div>
                    <div style="color: #64748b; font-size: 0.75rem; text-transform: uppercase; font-weight: 500;">Severity Score</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(htn_pct)

    ms_pct, ms_label, ms_crit = met_syndrome_score(
        bmi, ap_hi, ap_lo, gluc_mgdl, chol_mgdl
    )
    ms_color = (
        "#059669" if ms_pct < 50 else ("#d97706" if ms_pct < 75 else "#dc2626")
    )
    st.markdown(
        f"""
        <div class="result-card" style="padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 1.15rem; color: #0f172a; font-weight: 600;">Metabolic Syndrome</div>
                    <div style="color: #475569; font-size: 0.85rem; margin-top: 0.25rem;">NCEP ATP III Criteria: {ms_label} ({ms_crit}/4 risk factors)</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2rem; color: {ms_color}; font-weight: 700;">{ms_pct}/100</div>
                    <div style="color: #64748b; font-size: 0.75rem; text-transform: uppercase; font-weight: 500;">Criteria Index</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(ms_pct)

    cad_pct = cad_risk_calc(age, gender, chol_mgdl, ap_hi, cigs_per_day, bmi)
    cad_color = (
        "#059669" if cad_pct < 30 else ("#d97706" if cad_pct < 60 else "#dc2626")
    )
    st.markdown(
        f"""
        <div class="result-card" style="padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 1.15rem; color: #0f172a; font-weight: 600;">Coronary Artery Disease (CAD)</div>
                    <div style="color: #475569; font-size: 0.85rem; margin-top: 0.25rem;">Framingham Risk Factor Weighting Score</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2rem; color: {cad_color}; font-weight: 700;">{cad_pct}/100</div>
                    <div style="color: #64748b; font-size: 0.75rem; text-transform: uppercase; font-weight: 500;">Risk Score</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(cad_pct)

    stroke_pct = stroke_risk_calc(age, ap_hi, cigs_per_day, gluc_mgdl)
    stroke_color = (
        "#059669"
        if stroke_pct < 30
        else ("#d97706" if stroke_pct < 60 else "#dc2626")
    )
    st.markdown(
        f"""
        <div class="result-card" style="padding: 1.25rem 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 1.15rem; color: #0f172a; font-weight: 600;">Cerebrovascular / Stroke Risk</div>
                    <div style="color: #475569; font-size: 0.85rem; margin-top: 0.25rem;">Hypertension & Lifestyle Weighting Score</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2rem; color: {stroke_color}; font-weight: 700;">{stroke_pct}/100</div>
                    <div style="color: #64748b; font-size: 0.75rem; text-transform: uppercase; font-weight: 500;">Risk Score</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(stroke_pct)

    # 3. Contributing Factors List
    st.markdown(
        "<h3 style='margin-top: 2rem;'>Contributing Factors Breakdown</h3>",
        unsafe_allow_html=True,
    )
    factors = []
    if age > 55:
      factors.append(f"Age {age} (higher risk threshold)")
    if bmi >= 30:
      factors.append(f"BMI {bmi:.1f} (Obese range)")
    elif bmi >= 25:
      factors.append(f"BMI {bmi:.1f} (Overweight range)")
    if ap_hi >= 140 or ap_lo >= 90:
      factors.append(
          f"Blood Pressure {ap_hi}/{ap_lo} mmHg (Stage 2 Hypertension)"
      )
    elif ap_hi >= 130 or ap_lo >= 80:
      factors.append(
          f"Blood Pressure {ap_hi}/{ap_lo} mmHg (Elevated/Stage 1)"
      )
    if chol_mgdl >= 240:
      factors.append(f"Total Cholesterol {chol_mgdl} mg/dL (High ≥240)")
    elif chol_mgdl >= 200:
      factors.append(
          f"Total Cholesterol {chol_mgdl} mg/dL (Borderline 200-239)"
      )
    if gluc_mgdl >= 126:
      factors.append(
          f"Fasting Glucose {gluc_mgdl} mg/dL (Diabetic range ≥126)"
      )
    elif gluc_mgdl >= 100:
      factors.append(
          f"Fasting Glucose {gluc_mgdl} mg/dL (Prediabetic 100-125)"
      )
    if cigs_per_day > 0:
      factors.append(f"Tobacco use ({cigs_per_day} cigarettes/day)")
    if drinks_per_week >= 7:
      factors.append(f"Alcohol consumption ({drinks_per_week} drinks/week)")
    if exercise_min < 150:
      factors.append(
          f"Physical activity ({exercise_min} min/week — below WHO 150 min"
          " guideline)"
      )

    if factors:
      for f in factors:
        st.markdown(
            "<div style='padding: 0.5rem 0; color: #475569; border-bottom: 1px"
            f" solid #e2e8f0;'>→ {f}</div>",
            unsafe_allow_html=True,
        )
    else:
      st.markdown(
          "<div style='color: #059669; padding: 0.8rem 0; font-weight: 500;'>No"
          " major clinical risk factors identified.</div>",
          unsafe_allow_html=True,
      )

  else:
    if gene_data is None:
      st.warning("Please upload a gene expression CSV.")
      st.stop()

    for idx in gene_data.index:
      st.markdown(
          f"<h3 style='margin-top: 1.5rem;'>Sample: {idx}</h3>",
          unsafe_allow_html=True,
      )

      # Construct feature input vector
      gene_vector = pd.Series(0.0, index=GENE_COLUMNS)
      for gene in GENE_COLUMNS:
        if gene in gene_data.columns:
          gene_vector[gene] = gene_data.loc[idx, gene]

      clin_vector = pd.Series(0.0, index=CLIN_COLUMNS)
      X_input = pd.DataFrame([pd.concat([gene_vector, clin_vector])])

      # Predict probabilities
      probs = gene_pipeline.predict_proba(X_input)[0]

      class_probs = list(zip(encoder.classes_, probs))
      class_probs.sort(key=lambda x: x[1], reverse=True)

      for raw_cls, p in class_probs:
        pct = p * 100
        display_cls = raw_cls.replace("_", " ")

        if raw_cls == "Healthy":
          color = "#059669"
        elif raw_cls == "CAD":
          color = "#d97706"
        else:
          color = "#dc2626"

        st.markdown(
            f"""
                <div class="result-card" style="padding: 1.1rem 1.4rem; margin-bottom: 0.75rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <div style="font-size: 1.15rem; color: #0f172a; font-weight: 600;">{display_cls}</div>
                            <div style="color: #64748b; font-size: 0.8rem;">Multiclass Genomic Probability</div>
                        </div>
                        <div style="font-size: 2rem; color: {color}; font-weight: 700;">{pct:.1f}%</div>
                    </div>
                </div>
                """,
            unsafe_allow_html=True,
        )
        st.progress(min(100, max(0, int(round(pct)))))

  st.markdown("<hr>", unsafe_allow_html=True)
  st.info(
      "Research and educational tool only. Consult a physician for diagnostic"
      " advice."
  )

render_footer()
