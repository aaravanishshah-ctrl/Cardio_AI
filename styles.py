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
        /* ==== Prevent white flash during navigation ==== */
        html, body {
            background-color: #0a1628 !important;
            color: white;
        }
        
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
            background-color: #0a1628;
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
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] { background: transparent; }
        
        .stSpinner > div {
            border-top-color: #5eead4 !important;
        }
        
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
        /* NAVBAR — beautiful HTML with invisible button overlay */
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
            color: #94a3b8;
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
        /* INVISIBLE BUTTON OVERLAY TRICK                       */
        /* Hides Streamlit buttons but keeps them clickable     */
        /* ==================================================== */
        .invisible-nav-buttons {
            position: absolute;
            top: 1rem;
            left: 0;
            right: 0;
            z-index: 999;
            pointer-events: none;
        }
        .invisible-nav-buttons .stButton {
            pointer-events: auto;
        }
        .invisible-nav-buttons .stButton > button {
            background: transparent !important;
            color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
            height: 40px !important;
            cursor: pointer !important;
            font-size: 0 !important;
        }
        .invisible-nav-buttons .stButton > button:hover {
            background: transparent !important;
            transform: none !important;
            box-shadow: none !important;
        }
        .invisible-nav-buttons .stButton > button * {
            color: transparent !important;
            font-size: 0 !important;
        }
        
        /* HERO */
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
        
        /* HERO CTA BUTTONS — invisible overlay on styled divs */
        .hero-cta-visual {
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
            position: relative;
        }
        .hero-cta-primary {
            background: #5eead4;
            color: #0a1628 !important;
            padding: 0.9rem 2rem;
            border-radius: 10px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            display: inline-block;
            cursor: pointer;
            transition: all 0.2s;
        }
        .hero-cta-primary:hover {
            background: #6ee7d0;
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(94, 234, 212, 0.25);
        }
        .hero-cta-secondary {
            background: transparent;
            color: white !important;
            padding: 0.9rem 2rem;
            border-radius: 10px;
            font-weight: 600;
            border: 1px solid rgba(94, 234, 212, 0.3);
            display: inline-block;
            font-family: 'Inter', sans-serif;
            cursor: pointer;
            transition: all 0.2s;
        }
        .hero-cta-secondary:hover {
            background: rgba(94, 234, 212, 0.1);
            color: #5eead4 !important;
        }
        
        /* Invisible hero button overlay */
        .invisible-hero-buttons {
            position: relative;
            margin-top: -3.5rem;
            z-index: 999;
            pointer-events: none;
        }
        .invisible-hero-buttons .stButton {
            pointer-events: auto;
        }
        .invisible-hero-buttons .stButton > button {
            background: transparent !important;
            color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
            height: 50px !important;
            cursor: pointer !important;
            font-size: 0 !important;
        }
        .invisible-hero-buttons .stButton > button:hover {
            background: transparent !important;
            transform: none !important;
            box-shadow: none !important;
        }
        .invisible-hero-buttons .stButton > button * {
            color: transparent !important;
            font-size: 0 !important;
        }
        
        /* SECTION LABELS */
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
        
        /* STATS ROW */
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
        
        /* FEATURE CARDS */
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
        
        /* NORMAL BUTTONS (Predict, Begin Assessment on form pages) */
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
        
        /* NUMBER INPUTS */
        .stNumberInput input, .stTextInput input {
            background: #142943 !important;
            color: white !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 8px !important;
            padding: 0.6rem 0.9rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stNumberInput button {
            background: #142943 !important;
            color: white !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
        }
        .stNumberInput button:hover {
            background: rgba(94, 234, 212, 0.15) !important;
        }
        
        /* DROPDOWN FIX */
        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] > div > div,
        div[data-baseweb="select"] input {
            background-color: #142943 !important;
            color: white !important;
            border-color: rgba(94, 234, 212, 0.15) !important;
        }
        div[data-baseweb="select"] * {
            color: white !important;
            font-family: 'Inter', sans-serif !important;
        }
        div[data-baseweb="select"] div[role="button"] {
            background-color: #142943 !important;
            color: white !important;
        }
        div[data-baseweb="select"] svg {
            fill: #5eead4 !important;
            color: #5eead4 !important;
        }
        div[data-baseweb="popover"],
        div[role="listbox"],
        ul[role="listbox"] {
            background-color: #142943 !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
        }
        div[role="listbox"] *,
        ul[role="listbox"] * {
            background-color: #142943 !important;
            color: white !important;
            font-family: 'Inter', sans-serif !important;
        }
        li[role="option"]:hover,
        div[role="option"]:hover {
            background-color: rgba(94, 234, 212, 0.15) !important;
        }
        li[aria-selected="true"],
        div[aria-selected="true"] {
            background-color: rgba(94, 234, 212, 0.2) !important;
            color: #5eead4 !important;
        }
        
        /* LABELS */
        .stTextInput label, .stNumberInput label, .stSelectbox label, .stRadio label {
            color: #94a3b8 !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
        }
        
        /* RADIO */
        .stRadio [role="radiogroup"] { gap: 1rem; }
        .stRadio [role="radiogroup"] > label {
            background: #0f1e33;
            padding: 0.75rem 1.25rem;
            border-radius: 10px;
            border: 1px solid rgba(94, 234, 212, 0.15);
        }
        
        /* ALERTS */
        .stAlert {
            background: #0f1e33 !important;
            border: 1px solid rgba(94, 234, 212, 0.15) !important;
            border-radius: 10px !important;
        }
        .stAlert * { color: white !important; }
        
        /* PROGRESS BAR */
        .stProgress > div > div > div { background: #5eead4 !important; }
        .stProgress > div > div { background: #142943 !important; }
        
        /* FILE UPLOADER */
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
        
        /* RESULT CARDS */
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
        
        /* CITATIONS */
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
        
        /* FOOTER */
        .footer {
            margin-top: 5rem;
            padding: 2rem 0;
            border-top: 1px solid rgba(94, 234, 212, 0.15);
            text-align: center;
            color: #64748b;
            font-size: 0.85rem;
        }
    </style>
    """, unsafe_allow_html=True)


def render_navbar(active_page="home"):
    """Beautiful HTML navbar with invisible Streamlit buttons overlaid for fast nav."""
    
    # Step 1: Render beautiful HTML navbar (visuals only)
    nav_items = [
        ("screening", "Screening Tool"),
        ("clinical", "Clinical Reference"),
        ("clinicians", "For Clinicians"),
        ("about", "About"),
    ]
    
    links_html = ""
    for key, label in nav_items:
        cls = "active" if key == active_page else ""
        links_html += f'<span class="nav-item {cls}">{label}</span>'
    
    st.markdown(f"""
    <div class="navbar">
        <div class="navbar-logo">
            <span class="logo-icon"></span>
            CardioAI
        </div>
        <div class="navbar-links">
            {links_html}
        </div>
        <div class="navbar-cta">Start Screening →</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 2: Overlay invisible Streamlit buttons on top of the navbar
    st.markdown('<div class="invisible-nav-buttons">', unsafe_allow_html=True)
    col_logo, col_spacer, col1, col2, col3, col4, col_cta = st.columns([2, 0.5, 1.2, 1.4, 1.2, 0.8, 1.5])
    
    with col_logo:
        if st.button("logo", key="nav_logo"):
            st.switch_page("cardio_risk_app.py")
    with col1:
        if st.button("screening", key="nav_screening"):
            st.switch_page("pages/1_Screening_Tool.py")
    with col2:
        if st.button("clinical", key="nav_clinical"):
            st.switch_page("pages/2_Clinical_Reference.py")
    with col3:
        if st.button("clinicians", key="nav_clinicians"):
            st.switch_page("pages/3_For_Clinicians.py")
    with col4:
        if st.button("about", key="nav_about"):
            st.switch_page("pages/4_About.py")
    with col_cta:
        if st.button("cta", key="nav_cta"):
            st.switch_page("pages/1_Screening_Tool.py")
    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer">
        CardioAI — Research & educational tool. Not a diagnostic device.<br>
        © 2025 — Built with clinical decision support in mind.
    </div>
    """, unsafe_allow_html=True)
