# =============================================================================
# Shared styling module for CardioAI multi-page app.
# Clinical / Medical aesthetic + Custom SVG Logo + Mobile Responsive
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
            padding-top: 1.25rem;
            padding-bottom: 3rem;
            padding-left: 1.25rem;
            padding-right: 1.25rem;
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
        /* NAVBAR — DESKTOP                                     */
        /* ==================================================== */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0 1.1rem 0;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 2rem;
            background: transparent;
            flex-wrap: wrap;
            gap: 0.75rem;
        }
        .navbar-logo {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a !important;
            letter-spacing: -0.02em;
            white-space: nowrap;
            flex-shrink: 0;
        }
        .navbar-links {
            display: flex;
            gap: 1.75rem;
            font-size: 0.9rem;
            font-weight: 500;
            align-items: center;
        }
        .navbar-links span.nav-item {
            color: #475569 !important;
            cursor: pointer;
            transition: color 0.15s ease;
            white-space: nowrap;
        }
        .navbar-links span.nav-item:hover { color: #1e40af !important; }
        .navbar-links span.nav-item.active {
            color: #1e40af !important;
            font-weight: 600;
        }
        .navbar-cta {
            background: #1e40af;
            color: #ffffff !important;
            padding: 0.5rem 1.15rem;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.85rem;
            cursor: pointer;
            transition: background 0.15s ease;
            box-shadow: var(--shadow-sm);
            white-space: nowrap;
            flex-shrink: 0;
        }
        .navbar-cta:hover {
            background: #1e3a8a;
        }

        /* ==================================================== */
        /* NAVBAR — MOBILE / TABLET                             */
        /* ==================================================== */
        @media (max-width: 900px) {
            .navbar {
                flex-direction: column;
                align-items: stretch;
                gap: 0.85rem;
                padding-bottom: 1rem;
            }
            .navbar-logo {
                font-size: 1.15rem;
            }
            .navbar-links {
                display: flex;
                flex-wrap: wrap;
                justify-content: flex-start;
                gap: 0.65rem 1.1rem;
                width: 100%;
            }
            .navbar-links span.nav-item {
                font-size: 0.85rem;
            }
            .navbar-cta {
                width: 100%;
                text-align: center;
                padding: 0.65rem 1rem;
                font-size: 0.9rem;
            }
        }

        @media (max-width: 480px) {
            .navbar-links {
                gap: 0.5rem 0.9rem;
            }
            .navbar-links span.nav-item {
                font-size: 0.8rem;
            }
            .main .block-container {
                padding-left: 0.85rem;
                padding-right: 0.85rem;
            }
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

        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.15rem !important;
                line-height: 1.15 !important;
            }
            .hero-subtitle {
                font-size: 0.95rem;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 1.85rem !important;
            }
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

        @media (max-width: 768px) {
            .section-title {
                font-size: 1.5rem !important;
            }
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

        @media (max-width: 900px) {
            .stats-row {
                grid-template-columns: repeat(2, 1fr);
                gap: 1.25rem 1rem;
            }
            .feature-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .stats-row {
                grid-template-columns: 1fr 1fr;
            }
            .stat-number {
                font-size: 1.75rem;
            }
            .stat-label {
                font-size: 0.75rem;
            }
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
            width: auto !important;
        }
        .stButton > button:hover {
            background: #1e3a8a !important;
            transform: none !important;
            box-shadow: var(--shadow) !important;
        }
        .stButton > button * { color: #ffffff !important; }

        @media (max-width: 480px) {
            .stButton > button {
                width: 100% !important;
            }
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
        /* DROPDOWNS (SELECTBOX)                                */
        /* ==================================================== */
        div[data-testid="stSelectbox"] div[data-baseweb="select"],
        div[data-testid="stSelectbox"] div[data-baseweb="select"] *,
        div[data-baseweb="select"],
        div[data-baseweb="select"] *,
        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] > div *,
        div[data-baseweb="select"] [role="button"],
        div[data-baseweb="select"] [role="button"] * {
            background-color: #ffffff !important;
            background: #ffffff !important;
            color: #0f172a !important;
            -webkit-text-fill-color: #0f172a !important;
        }

        div[data-testid="stSelectbox"] [data-baseweb="select"] > div:first-child {
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            min-height: 42px !important;
            box-shadow: var(--shadow-sm) !important;
        }

        div[data-baseweb="select"] svg,
        div[data-baseweb="select"] svg * {
            fill: #1e40af !important;
            color: #1e40af !important;
        }

        div[data-baseweb="popover"],
        div[data-baseweb="popover"] *,
        div[role="listbox"],
        ul[role="listbox"] {
            background-color: #ffffff !important;
            background: #ffffff !important;
            color: #0f172a !important;
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
            color: #1e40af !important;
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

        @media (max-width: 480px) {
            .risk-score-huge {
                font-size: 2.5rem;
            }
            .result-card {
                padding: 1.15rem 1.25rem;
            }
        }

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
        /* HERO BUTTON OVERRIDES                                */
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

        @media (max-width: 480px) {
            a[href*="goto=screening"] > div,
            a[href*="goto=clinical"] > div {
                width: 100% !important;
                text-align: center !important;
                box-sizing: border-box !important;
            }
        }
    </style>
    """,
      unsafe_allow_html=True,
  )


def render_navbar(active_page="home"):
  """Clean clinical navbar with custom SVG Logo — mobile responsive."""

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
                <svg width="30" height="30" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;">
                    <rect width="32" height="32" rx="8" fill="#1E40AF"/>
                    <path d="M16 25.5C16 25.5 7 19 7 12.5C7 9.46243 9.46243 7 12.5 7C14.3644 7 16 7.92543 16 9.5C16 7.92543 17.6356 7 19.5 7C22.5376 7 25 9.46243 25 12.5C25 19 16 25.5 16 25.5Z" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                    <path d="M10.5 15H13L14.5 11.5L17 18.5L18.5 15H21.5" stroke="#93C5FD" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
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
