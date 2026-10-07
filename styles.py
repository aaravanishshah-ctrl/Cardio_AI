# =============================================================================
# Shared styling module for CardioAI multi-page app.
# Clinical / Medical aesthetic (Epic / UpToDate / Mayo Clinic inspired)
# =============================================================================

import streamlit as st


def apply_styles():
  st.markdown(
      """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* ==================================================== */
        /* ROOT & GLOBAL BACKGROUND                             */
        /* ==================================================== */
        html, body, #root, .stApp, .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        iframe {
            background-color: #f8fafc !important;
            color: #0f172a !important;
        }

        html, body {
            background: #f8fafc !important;
        }

        :root {
            --bg-page: #f8fafc;
            --bg-card: #ffffff;
            --bg-muted: #f1f5f9;
            --primary: #1e40af;
            --primary-hover: #1e3a8a;
            --primary-soft: #dbeafe;
            --primary-border: #bfdbfe;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --success: #059669;
            --warning: #d97706;
            --danger: #dc2626;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            --radius: 8px;
        }

        .stApp {
            background-color: #f8fafc !important;
            background-image: none !important;
        }

        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1100px;
        }

        /* Hide Streamlit chrome */
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        header[data-testid="stHeader"] {
            background: transparent !important;
            display: none !important;
        }
        [data-testid="stDecoration"] { display: none !important; }
        [data-testid="stToolbar"] { display: none !important; }
        [data-testid="stStatusWidget"] { display: none !important; }
        .stAppHeader { display: none !important; }
        div[class*="viewerBadge"] { display: none !important; }
        a[href*="streamlit.io"] { display: none !important; }
        .stApp > header { display: none !important; }
        section[data-testid="stSidebar"] { display: none !important; }
        button[kind="header"] { display: none !important; }

        .stSpinner > div { border-top-color: #1e40af !important; }

        /* ==================================================== */
        /* TYPOGRAPHY                                           */
        /* ==================================================== */
        html, body, [class*="css"], p, div, span, label, li {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            color: #0f172a !important;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            color: #0f172a !important;
            font-weight: 700 !important;
            letter-spacing: -0.025em;
        }

        /* ==================================================== */
        /* NAVBAR                                               */
        /* ==================================================== */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.85rem 0 1.25rem 0;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 2.5rem;
            background: transparent;
        }
        .navbar-logo {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a !important;
            letter-spacing: -0.02em;
        }
        .logo-icon {
            width: 28px;
            height: 28px;
            background: #1e40af;
            border-radius: 6px;
            display: inline-block;
        }
        .navbar-links {
            display: flex;
            gap: 2rem;
            font-size: 0.9rem;
            font-weight: 500;
        }
        .navbar-links span.nav-item {
            color: #475569 !important;
            cursor: pointer;
            transition: color 0.15s ease;
        }
        .navbar-links span.nav-item:hover { color: #1e40af !important; }
        .navbar-links span.nav-item.active {
            color: #1e40af !important;
            font-weight: 600;
        }
        .navbar-cta {
            background: #1e40af;
            color: #ffffff !important;
            padding: 0.55rem 1.25rem;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            transition: background 0.15s ease;
            box-shadow: var(--shadow-sm);
        }
        .navbar-cta:hover {
            background: #1e3a8a;
        }

        /* ==================================================== */
        /* HERO                                                 */
        /* ==================================================== */
        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.35rem 0.9rem;
            background: #dbeafe;
            border: 1px solid #bfdbfe;
            border-radius: 999px;
            color: #1e40af !important;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 1.25rem;
        }
        .hero-pill::before {
            content: "";
            width: 6px;
            height: 6px;
            background: #1e40af;
            border-radius: 50%;
        }
        .hero-title {
            font-size: 3.25rem !important;
            line-height: 1.1 !important;
            font-weight: 700 !important;
            color: #0f172a !important;
            margin: 0 0 1.25rem 0 !important;
            letter-spacing: -0.03em;
        }
        .hero-title-accent {
            color: #1e40af !important;
            font-style: normal !important;
            font-weight: 700 !important;
        }
        .hero-subtitle {
            font-size: 1.05rem;
            line-height: 1.65;
            color: #475569 !important;
            max-width: 640px;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        /* ==================================================== */
        /* SECTION LABELS                                       */
        /* ==================================================== */
        .section-label {
            color: #1e40af !important;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }
        .section-title {
            font-size: 2rem !important;
            color: #0f172a !important;
            line-height: 1.2 !important;
            margin-bottom: 1rem !important;
            font-weight: 700 !important;
        }
        .section-subtitle {
            font-size: 1rem;
            color: #475569 !important;
            line-height: 1.65;
            max-width: 680px;
            margin-bottom: 2.5rem;
        }

        /* ==================================================== */
        /* STATS + FEATURES                                     */
        /* ==================================================== */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            padding: 1.75rem 0;
            border-top: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
            margin: 2.5rem 0;
            background: transparent;
        }
        .stat-item { text-align: center; }
        .stat-number {
            font-size: 2.25rem;
            font-weight: 700;
            color: #1e40af !important;
            line-height: 1.1;
            margin-bottom: 0.4rem;
            letter-spacing: -0.02em;
        }
        .stat-label {
            color: #64748b !important;
            font-size: 0.8rem;
            line-height: 1.4;
            font-weight: 500;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.25rem;
            padding: 0;
            background: transparent;
            border: none;
            border-radius: 0;
            margin: 1.5rem 0 2.5rem 0;
        }
        .feature-card {
            padding: 1.5rem;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.15s ease, border-color 0.15s ease;
        }
        .feature-card:hover {
            box-shadow: var(--shadow);
            border-color: #bfdbfe;
        }
        .feature-icon {
            width: 42px;
            height: 42px;
            background: #dbeafe;
            border: 1px solid #bfdbfe;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            margin-bottom: 1.1rem;
        }
        .feature-title {
            font-size: 1.1rem;
            color: #0f172a !important;
            font-weight: 600;
            margin-bottom: 0.5rem;
            letter-spacing: -0.01em;
        }
        .feature-desc {
            color: #475569 !important;
            font-size: 0.9rem;
            line-height: 1.55;
        }

        /* ==================================================== */
        /* MAIN BUTTONS                                         */
        /* ==================================================== */
        .stButton > button {
            background: #1e40af !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.7rem 1.6rem !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            transition: background 0.15s ease !important;
            box-shadow: var(--shadow-sm) !important;
        }
        .stButton > button:hover {
            background: #1e3a8a !important;
            transform: none !important;
            box-shadow: var(--shadow) !important;
        }
        .stButton > button * { color: #ffffff !important; }

        /* ==================================================== */
        /* WIDGET WRAPPERS                                      */
        /* ==================================================== */
        [data-testid="stSelectbox"],
        [data-testid="stNumberInput"],
        [data-testid="stTextInput"],
        [data-testid="stRadio"],
        [data-testid="stFileUploader"],
        div[data-testid="stSelectbox"] > div,
        div[data-testid="stNumberInput"] > div,
        div[data-testid="stTextInput"] > div,
        div[data-testid="element-container"] {
            background-color: transparent !important;
            background: transparent !important;
        }

        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] * {
            background-color: transparent !important;
            background: transparent !important;
        }

        /* ==================================================== */
        /* NUMBER + TEXT INPUTS                                 */
        /* ==================================================== */
        .stNumberInput input, .stTextInput input {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            padding: 0.55rem 0.85rem !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.95rem !important;
            box-shadow: var(--shadow-sm) !important;
        }
        .stNumberInput input:focus, .stTextInput input:focus {
            border-color: #1e40af !important;
            box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.12) !important;
        }
        .stNumberInput button {
            background-color: #f1f5f9 !important;
            color: #0f172a !important;
            border: 1px solid #e2e8f0 !important;
        }
        .stNumberInput button:hover {
            background-color: #e2e8f0 !important;
        }

        /* ==================================================== */
        /* DROPDOWNS                                            */
        /* ==================================================== */
        div[data-baseweb="select"] > div:first-child {
            background-color: #ffffff !important;
            background: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            min-height: 40px !important;
            box-shadow: var(--shadow-sm) !important;
        }
        div[data-baseweb="select"] div[role="button"],
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] input {
            color: #0f172a !important;
            -webkit-text-fill-color: #0f172a !important;
            background-color: transparent !important;
        }
        div[data-baseweb="select"] svg {
            fill: #64748b !important;
            color: #64748b !important;
        }
        div[data-baseweb="popover"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            box-shadow: var(--shadow-md) !important;
        }
        div[data-baseweb="popover"] > div,
        div[role="listbox"],
        ul[role="listbox"] {
            background-color: #ffffff !important;
        }
        li[role="option"], div[role="option"] {
            background-color: #ffffff !important;
            color: #0f172a !important;
            -webkit-text-fill-color: #0f172a !important;
            font-family: 'Inter', sans-serif !important;
            padding: 0.55rem 0.9rem !important;
        }
        li[role="option"]:hover, div[role="option"]:hover {
            background-color: #f1f5f9 !important;
        }
        li[aria-selected="true"], div[aria-selected="true"] {
            background-color: #dbeafe !important;
        }
        li[aria-selected="true"] *, div[aria-selected="true"] * {
            color: #1e40af !important;
            -webkit-text-fill-color: #1e40af !important;
        }

        /* ==================================================== */
        /* LABELS                                               */
        /* ==================================================== */
        .stTextInput label, .stNumberInput label, .stSelectbox label, .stRadio label,
        [data-testid="stWidgetLabel"] label,
        [data-testid="stWidgetLabel"] p {
            color: #475569 !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            background-color: transparent !important;
        }

        /* ==================================================== */
        /* RADIO BUTTONS                                        */
        /* ==================================================== */
        .stRadio [role="radiogroup"] { gap: 0.75rem; }
        .stRadio [role="radiogroup"] > label {
            background: #ffffff !important;
            padding: 0.65rem 1.1rem;
            border-radius: 6px;
            border: 1px solid #e2e8f0 !important;
            box-shadow: var(--shadow-sm);
        }
        .stRadio [role="radiogroup"] > label * {
            color: #0f172a !important;
        }
        div[data-baseweb="radio"] div[role="radio"] {
            background-color: transparent !important;
            border: 2px solid #94a3b8 !important;
        }
        div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] {
            background-color: #1e40af !important;
            border-color: #1e40af !important;
        }
        div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] > div {
            background-color: #ffffff !important;
        }
        .stRadio input[type="radio"]:checked {
            accent-color: #1e40af !important;
        }

        /* ==================================================== */
        /* ALERTS, PROGRESS, FILE UPLOADER                      */
        /* ==================================================== */
        .stAlert {
            background: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px !important;
            box-shadow: var(--shadow-sm) !important;
        }
        .stAlert * { color: #0f172a !important; }

        .stProgress > div > div > div { background: #1e40af !important; }
        .stProgress > div > div { background: #e2e8f0 !important; }

        [data-testid="stFileUploaderDropzone"] {
            background: #ffffff !important;
            border: 1.5px dashed #cbd5e1 !important;
            border-radius: 8px !important;
            box-shadow: var(--shadow-sm) !important;
        }
        [data-testid="stFileUploaderDropzone"] * {
            color: #64748b !important;
            font-family: 'Inter', sans-serif !important;
        }
        [data-testid="stFileUploaderDropzone"] button {
            background: #1e40af !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.45rem 1.1rem !important;
            font-weight: 600 !important;
            box-shadow: var(--shadow-sm) !important;
        }
        [data-testid="stFileUploaderDropzone"] button p {
            color: #ffffff !important;
        }
        [data-testid="stFileUploaderDropzone"] button::before,
        [data-testid="stFileUploaderDropzone"] button span.material-icons,
        [data-testid="stFileUploaderDropzone"] button span[class*="material"] {
            display: none !important;
            content: none !important;
        }

        /* ==================================================== */
        /* RESULT CARDS + CITATIONS                             */
        /* ==================================================== */
        .result-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 1.5rem 1.75rem;
            margin: 1rem 0;
            box-shadow: var(--shadow-sm);
        }
        .risk-score-huge {
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1;
            margin: 0.4rem 0;
            letter-spacing: -0.03em;
            color: #0f172a;
        }
        .citation-block {
            background: #f8fafc;
            border-left: 3px solid #1e40af;
            padding: 1.25rem 1.5rem;
            border-radius: 0 8px 8px 0;
            margin: 1.25rem 0;
            font-size: 0.9rem;
            line-height: 1.6;
            color: #475569;
            border: 1px solid #e2e8f0;
            border-left: 3px solid #1e40af;
        }
        .citation-block * { color: #475569 !important; }

        hr {
            border: none;
            border-top: 1px solid #e2e8f0;
            margin: 2.5rem 0;
        }

        .footer {
            margin-top: 4rem;
            padding: 1.75rem 0;
            border-top: 1px solid #e2e8f0;
            text-align: center;
            color: #64748b !important;
            font-size: 0.8rem;
            font-weight: 500;
        }
        .footer * {
            color: #64748b !important;
        }

        /* ==================================================== */
        /* HERO BUTTON OVERRIDES (Home page inline styles)      */
        /* ==================================================== */
        a[href*="goto=screening"] > div {
            background: #1e40af !important;
            color: #ffffff !important;
            border-radius: 6px !important;
            box-shadow: var(--shadow-sm) !important;
        }
        a[href*="goto=screening"] > div:hover {
            background: #1e3a8a !important;
            transform: none !important;
        }
        a[href*="goto=clinical"] > div {
            background: #ffffff !important;
            color: #0f172a !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
        }
        a[href*="goto=clinical"] > div:hover {
            background: #f1f5f9 !important;
            color: #1e40af !important;
            border-color: #bfdbfe !important;
        }
    </style>
    """,
      unsafe_allow_html=True,
  )


def render_navbar(active_page="home"):
  """Clean clinical navbar. Navigation via query params + st.switch_page()."""

  if "nav" in st.query_params:
    target = st.query_params["nav"]
    st.query_params.clear()
    nav_map = {
        "home": "cardio_risk_app.py",
        "screening": "pages/1_Screening_Tool.py",
        "clinical": "pages/2_Clinical_Reference.py",
        "clinicians": "pages/3_For_Clinicians.py",
        "about": "pages/4_About.py",
    }
    if target in nav_map:
      st.switch_page(nav_map[target])

  nav_items = [
      ("screening", "Screening Tool"),
      ("clinical", "Clinical Reference"),
      ("clinicians", "For Clinicians"),
      ("about", "About"),
  ]

  links_html = ""
  for key, label in nav_items:
    cls = "active" if key == active_page else ""
    links_html += (
        f'<a href="?nav={key}" target="_self" style="text-decoration:none;">'
        f'<span class="nav-item {cls}">{label}</span></a>'
    )

  st.markdown(
      f"""
    <div class="navbar">
        <a href="?nav=home" target="_self" style="text-decoration:none;">
            <div class="navbar-logo">
                <span class="logo-icon"></span>
                CardioAI
            </div>
        </a>
        <div class="navbar-links">
            {links_html}
        </div>
        <a href="?nav=screening" target="_self" style="text-decoration:none;">
            <div class="navbar-cta">Start Screening →</div>
        </a>
    </div>
    """,
      unsafe_allow_html=True,
  )


def render_footer():
  st.markdown(
      """
    <div class="footer">
        CardioAI — Research &amp; educational tool. Not a diagnostic device.<br>
        © 2025 — Built for clinical decision support.
    </div>
    """,
      unsafe_allow_html=True,
  )
