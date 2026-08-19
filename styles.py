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
        
        /* Loading spinner in theme color */
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
        
        /* NAVBAR */
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
            gap: 2rem;
            color: #94a3b8;
            font-size: 0.95rem;
        }
        .navbar-links a { 
            color: #94a3b8 !important; 
            text-decoration: none; 
            transition: color 0.2s;
        }
        .navbar-links a:hover { color: #5eead4 !important; }
        .navbar-links a.active { color: #5eead4 !important; }
        
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
        
        /* BUTTONS */
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
        .stButton > button * { color: #0a1628 !important; } /* ============================================ */
/* NAVBAR BUTTONS — styled to look like links   */
/* ============================================ */

/* Navbar link-style buttons (Screening Tool, Clinical Reference, etc.) */
.nav-link-btn button {
    background: transparent !important;
    color: #94a3b8 !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0.5rem 0.75rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 400 !important;
    font-size: 0.95rem !important;
    transition: color 0.2s !important;
}
.nav-link-btn button:hover {
    background: transparent !important;
    color: #5eead4 !important;
    transform: none !important;
    box-shadow: none !important;
}
.nav-link-btn button * {
    color: inherit !important;
}
.nav-link-btn.active button {
    color: #5eead4 !important;
}

/* Logo button (top-left) */
.nav-logo-btn button {
    background: transparent !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    text-align: left !important;
    justify-content: flex-start !important;
}
.nav-logo-btn button:hover {
    background: transparent !important;
    color: #5eead4 !important;
    transform: none !important;
    box-shadow: none !important;
}
.nav-logo-btn button * {
    color: inherit !important;
}

/* CTA button (Start Screening, top-right) */
.nav-cta-btn button {
    background: #5eead4 !important;
    color: #0a1628 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.4rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    transition: all 0.2s !important;
}
.nav-cta-btn button:hover {
    background: #6ee7d0 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(94, 234, 212, 0.25) !important;
}
.nav-cta-btn button * {
    color: #0a1628 !important;
}

/* Secondary button (outlined) — for "Explore features" */
.secondary-btn button {
    background: transparent !important;
    color: white !important;
    border: 1px solid rgba(94, 234, 212, 0.3) !important;
}
.secondary-btn button:hover {
    background: rgba(94, 234, 212, 0.1) !important;
    color: #5eead4 !important;
}
.secondary-btn button * { color: inherit !important; }
        
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
        
        /* HIDE SIDEBAR NAV */
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
    """Renders the top navbar using native Streamlit buttons for fast navigation."""
    
    col_logo, col_spacer, col_links, col_cta = st.columns([2, 1, 4, 1.5])
    
    with col_logo:
        st.markdown('<div class="nav-logo-btn">', unsafe_allow_html=True)
        if st.button("● CardioAI", key="nav_logo"):
            st.switch_page("cardio_risk_app.py")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_links:
        subcol1, subcol2, subcol3, subcol4 = st.columns(4)
        
        with subcol1:
            active_cls = "active" if active_page == "screening" else ""
            st.markdown(f'<div class="nav-link-btn {active_cls}">', unsafe_allow_html=True)
            if st.button("Screening Tool", key="nav_screening"):
                st.switch_page("pages/1_Screening_Tool.py")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with subcol2:
            active_cls = "active" if active_page == "clinical" else ""
            st.markdown(f'<div class="nav-link-btn {active_cls}">', unsafe_allow_html=True)
            if st.button("Clinical Reference", key="nav_clinical"):
                st.switch_page("pages/2_Clinical_Reference.py")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with subcol3:
            active_cls = "active" if active_page == "clinicians" else ""
            st.markdown(f'<div class="nav-link-btn {active_cls}">', unsafe_allow_html=True)
            if st.button("For Clinicians", key="nav_clinicians"):
                st.switch_page("pages/3_For_Clinicians.py")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with subcol4:
            active_cls = "active" if active_page == "about" else ""
            st.markdown(f'<div class="nav-link-btn {active_cls}">', unsafe_allow_html=True)
            if st.button("About", key="nav_about"):
                st.switch_page("pages/4_About.py")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col_cta:
        st.markdown('<div class="nav-cta-btn">', unsafe_allow_html=True)
        if st.button("Start Screening →", key="nav_cta"):
            st.switch_page("pages/1_Screening_Tool.py")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 1rem 0 3rem 0;'>", unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer">
        CardioAI — Research & educational tool. Not a diagnostic device.<br>
        © 2025 — Built with clinical decision support in mind.
    </div>
    """, unsafe_allow_html=True)
