# =============================================================================
# Shared styling module for CardioAI multi-page app.
# =============================================================================

import streamlit as st

def apply_styles():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        html, body, #root, .stApp, .main, .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        iframe {
            background-color: #0a1628 !important;
            color: white;
        }
        
        html { background: #0a1628 !important; }
        body { background: #0a1628 !important; }
        
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
        
        .stApp {
            background-color: #0a1628 !important;
            background-image: 
                linear-gradient(rgba(94, 234, 212, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(94, 234, 212, 0.03) 1px, transparent 1px);
            background-size: 60px 60px;
        }
        
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }
        
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
        
        .stSpinner > div { border-top-color: #5eead4 !important; }
        
        html, body, [class*="css"], p, div, span, label, li {
            font-family: 'Inter', -apple-system, sans-serif !important;
            color: #ffffff !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Playfair Display', Georgia, serif !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }
        
        /* ==================================================== */
        /* NAVBAR                                               */
        /* ==================================================== */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0 2rem 0;
            border-bottom: 1px solid rgba(94, 234, 212, 0.15);
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
            background: #5eead4;
            border-radius: 8px;
            display: inline-block;
        }
        .navbar-links {
            display: flex;
            gap: 2.5rem;
            font-size: 0.95rem;
        }
        .navbar-links span.nav-item {
            color: #94a3b8;
            cursor: pointer;
            transition: color 0.2s;
            font-family: 'Inter', sans-serif;
        }
        .navbar-links span.nav-item:hover { color: #5eead4; }
        .navbar-links span.nav-item.active { color: #5eead4; }
        .navbar-cta {
            background: #5eead4;
            color: #0a1628 !important;
            padding: 0.6rem 1.4rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: all 0.2s;
        }
        .navbar-cta:hover {
            background: #6ee7d0;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(94, 234, 212, 0.25);
        }
        
        /* ==================================================== */
        /* HERO                                                 */
        /* ==================================================== */
        .hero-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 1rem;
            border: 1px solid #5eead4;
            border-radius: 999px;
            color: #5eead4 !important;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
        }
        .hero-pill::before {
            content: "";
            width: 6px; height: 6px;
            background: #5eead4;
            border-radius: 50%;
        }
        .hero-title {
            font-family: 'Playfair Display', serif !important;
            font-size: 4rem !important;
            line-height: 1.05 !important;
            font-weight: 700 !important;
            color: white !important;
            margin: 0 0 1.5rem 0 !important;
            letter-spacing: -0.03em;
        }
        .hero-title-accent {
            color: #5eead4 !important;
            font-style: italic;
            font-weight: 400 !important;
        }
        .hero-subtitle {
            font-family: 'Inter', sans-serif !important;
            font-size: 1.1rem;
            line-height: 1.6;
            color: #94a3b8 !important;
            max-width: 620px;
            margin-bottom: 2.5rem;
        }
        
        /* ==================================================== */
        /* SECTION LABELS                                       */
        /* ==================================================== */
        .section-label {
            color: #5eead4 !important;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }
        .section-title {
            font-family: 'Playfair Display', serif !important;
            font-size: 2.5rem !important;
            color: white !important;
            line-height: 1.15 !important;
            margin-bottom: 1.5rem !important;
        }
        .section-subtitle {
            font-size: 1.05rem;
            color: #94a3b8 !important;
            line-height: 1.7;
            max-width: 700px;
            margin-bottom: 3rem;
        }
        
        /* ==================================================== */
        /* STATS + FEATURES                                     */
        /* ==================================================== */
        .stats-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            padding: 2rem 0;
            border-top: 1px solid rgba(94, 234, 212, 0.15);
            border-bottom: 1px solid rgba(94, 234, 212, 0.15);
            margin: 3rem 0;
        }
        .stat-item { text-align: center; }
        .stat-number {
            font-family: 'Playfair Display', serif;
            font-size: 2.8rem;
            font-weight: 700;
            color: #5eead4 !important;
            line-height: 1;
            margin-bottom: 0.5rem;
        }
        .stat-label {
            color: #94a3b8 !important;
            font-size: 0.85rem;
            line-height: 1.4;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            padding: 2rem;
            background: #0f1e33;
            border: 1px solid rgba(94, 234, 212, 0.15);
            border-radius: 16px;
            margin: 2rem 0;
        }
        .feature-card { padding: 1.5rem; }
        .feature-icon {
            width: 48px;
            height: 48px;
            background: rgba(94, 234, 212, 0.15);
            border: 1px solid rgba(94, 234, 212, 0.15);
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
            color: white !important;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }
        .feature-desc {
            color: #94a3b8 !important;
            font-size: 0.95rem;
            line-height: 1.6;
        }
        
        /* ==================================================== */
        /* MAIN BUTTONS                                         */
        /* ==================================================== */
        .stButton > button {
            background: #5eead4 !important;
            color: #0a1628 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.9rem 2rem !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            transition: all 0.2s !important;
        }
        .stButton > button:hover {
            background: #6ee7d0 !important;
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(94, 234, 212, 0.25);
        }
        .stButton > button * { color: #0a1628 !important; }
        
        /* ==================================================== */
        /* CRITICAL: Make ALL widget WRAPPERS transparent       */
        /* This removes the lighter blue "halo" behind labels   */
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
        
        /* Labels should also have transparent bg */
        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] * {
            background-color: transparent !important;
            background: transparent !important;
        }
        
        /* ==================================================== */
        /* NUMBER + TEXT INPUTS — the visible box               */
        /* ==================================================== */
        .stNumberInput input, .stTextInput input {
            background-color: #142943 !important;
            color: white !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 8px !important;
            padding: 0.6rem 0.9rem !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 1rem !important;
        }
        .stNumberInput button {
            background-color: #142943 !important;
            color: white !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
        }
        .stNumberInput button:hover {
            background-color: rgba(94, 234, 212, 0.15) !important;
        }
        
        /* ==================================================== */
        /* DROPDOWN — make the input box match number inputs   */
        /* ==================================================== */
        
        /* The visible box (BaseWeb select control) */
        div[data-baseweb="select"] > div:first-child {
            background-color: #142943 !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 8px !important;
            min-height: 42px !important;
            padding: 0.1rem 0.5rem !important;
        }
        
        /* KILL the opacity on selected value — was showing text as faded */
        div[data-baseweb="select"] div[role="button"],
        div[data-baseweb="select"] div[role="button"] *,
        div[data-baseweb="select"] div[data-baseweb="select-option"],
        div[data-baseweb="select"] [class*="valueContainer"],
        div[data-baseweb="select"] [class*="singleValue"],
        div[data-baseweb="select"] [class*="ValueContainer"] {
            color: #ffffff !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #ffffff !important;
            background-color: transparent !important;
        }
        
        /* All spans, text inside the selected value display */
        div[data-baseweb="select"] span {
            color: #ffffff !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        
        /* Hidden input */
        div[data-baseweb="select"] input {
            color: #ffffff !important;
            background-color: transparent !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        
        /* Chevron */
        div[data-baseweb="select"] svg {
            fill: #5eead4 !important;
            color: #5eead4 !important;
            opacity: 1 !important;
        }
        
        /* Opened menu */
        div[data-baseweb="popover"] {
            background-color: #142943 !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 8px !important;
        }
        div[data-baseweb="popover"] * {
            background-color: transparent !important;
        }
        div[role="listbox"], ul[role="listbox"] {
            background-color: #142943 !important;
            border: none !important;
        }
        li[role="option"], div[role="option"] {
            background-color: transparent !important;
            color: #ffffff !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #ffffff !important;
            font-family: 'Inter', sans-serif !important;
            padding: 0.6rem 1rem !important;
        }
        li[role="option"] *, div[role="option"] * {
            color: #ffffff !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #ffffff !important;
            background-color: transparent !important;
        }
        li[role="option"]:hover, div[role="option"]:hover {
            background-color: rgba(94, 234, 212, 0.15) !important;
        }
        li[aria-selected="true"], div[aria-selected="true"] {
            background-color: rgba(94, 234, 212, 0.2) !important;
        }
        li[aria-selected="true"] *, div[aria-selected="true"] * {
            color: #5eead4 !important;
            -webkit-text-fill-color: #5eead4 !important;
        }
        
        /* ==================================================== */
        /* LABELS above inputs — no bg, just white text         */
        /* ==================================================== */
        .stTextInput label, .stNumberInput label, .stSelectbox label, .stRadio label,
        [data-testid="stWidgetLabel"] label,
        [data-testid="stWidgetLabel"] p {
            color: #94a3b8 !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            background-color: transparent !important;
            background: transparent !important;
        }
        
        /* ==================================================== */
        /* RADIO BUTTONS                                        */
        /* ==================================================== */
        .stRadio [role="radiogroup"] { gap: 1rem; }
        .stRadio [role="radiogroup"] > label {
            background: #142943 !important;
            padding: 0.75rem 1.25rem;
            border-radius: 10px;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
        }
        .stRadio [role="radiogroup"] > label * {
            color: white !important;
        }
        div[data-baseweb="radio"] div[role="radio"] {
            background-color: transparent !important;
            border: 2px solid rgba(94, 234, 212, 0.5) !important;
        }
        div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] {
            background-color: #5eead4 !important;
            border-color: #5eead4 !important;
        }
        div[data-baseweb="radio"] div[role="radio"][aria-checked="true"] > div {
            background-color: #0a1628 !important;
        }
        .stRadio input[type="radio"]:checked {
            accent-color: #5eead4 !important;
        }
        
        /* ==================================================== */
        /* ALERTS, PROGRESS, FILE UPLOADER                      */
        /* ==================================================== */
        .stAlert {
            background: #0f1e33 !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 10px !important;
        }
        .stAlert * { color: white !important; }
        
        .stProgress > div > div > div { background: #5eead4 !important; }
        .stProgress > div > div { background: #142943 !important; }
        
        [data-testid="stFileUploaderDropzone"] {
            background: #0f1e33 !important;
            border: 2px dashed rgba(94, 234, 212, 0.15) !important;
            border-radius: 10px !important;
        }
        [data-testid="stFileUploaderDropzone"] * {
            color: #94a3b8 !important;
            font-family: 'Inter', sans-serif !important;
        }
        [data-testid="stFileUploaderDropzone"] button {
            background: #5eead4 !important;
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
        
        /* ==================================================== */
        /* RESULT CARDS + CITATIONS                             */
        /* ==================================================== */
        .result-card {
            background: #0f1e33;
            border: 1px solid rgba(94, 234, 212, 0.15);
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
        .citation-block {
            background: #0f1e33;
            border-left: 3px solid #5eead4;
            padding: 1.5rem 2rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            font-size: 0.9rem;
            line-height: 1.7;
            color: #94a3b8;
        }
        .citation-block * { color: #94a3b8 !important; }
        
        section[data-testid="stSidebar"] { display: none !important; }
        button[kind="header"] { display: none !important; }
        
        hr {
            border: none;
            border-top: 1px solid rgba(94, 234, 212, 0.15);
            margin: 3rem 0;
        }
        
        .footer {
            margin-top: 5rem;
            padding: 2rem 0;
            border-top: 1px solid rgba(94, 234, 212, 0.15);
            text-align: center;
            color: #64748b;
            font-size: 0.85rem;
        }
    </style>
    
    <script>
        document.documentElement.style.backgroundColor = '#0a1628';
        document.body.style.backgroundColor = '#0a1628';
    </script>
    """, unsafe_allow_html=True)


def render_navbar(active_page="home"):
    """Beautiful HTML navbar. Navigation via query params + st.switch_page()."""
    
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
        links_html += f'<a href="?nav={key}" target="_self" style="text-decoration:none;"><span class="nav-item {cls}">{label}</span></a>'
    
    st.markdown(f"""
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
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer">
        CardioAI — Research & educational tool. Not a diagnostic device.<br>
        © 2025 — Built with clinical decision support in mind.
    </div>
    """, unsafe_allow_html=True)
