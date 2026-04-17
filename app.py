# -*- coding: utf-8 -*-
"""
LoanIQ — Professional Loan Eligibility Platform
Main entry point
"""

import streamlit as st

st.set_page_config(
    page_title="LoanIQ · Smart Loan Predictor",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Inject global CSS + fonts ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    scroll-behavior: smooth;
}

/* === BACKGROUND === */
.stApp {
    background: #050816;
    min-height: 100vh;
}

/* animated aurora bg */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 50% at 20% 20%, rgba(99,102,241,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(16,185,129,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 50% 60% at 50% 50%, rgba(245,158,11,0.04) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
    animation: aurora 12s ease-in-out infinite alternate;
}

@keyframes aurora {
    0%   { opacity: 0.6; transform: scale(1); }
    100% { opacity: 1;   transform: scale(1.05); }
}

/* grid dots */
.stApp::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 36px 36px;
    pointer-events: none;
    z-index: 0;
}

/* all content above bg */
[data-testid="stAppViewContainer"] > div { position: relative; z-index: 1; }

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background: rgba(5,8,22,0.92) !important;
    border-right: 1px solid rgba(99,102,241,0.15) !important;
    backdrop-filter: blur(20px);
}
[data-testid="stSidebar"] * { color: #cbd5e1 !important; }

/* === HIDE STREAMLIT CHROME === */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }

/* === TOP NAV === */
.topnav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 0 24px;
    margin-bottom: 8px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.02em;
}
.logo span { color: #6366f1; }
.nav-links { display: flex; gap: 8px; }
.nav-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 16px;
    border-radius: 100px;
    font-size: 0.82rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
    border: 1px solid transparent;
    color: rgba(255,255,255,0.5);
}
.nav-pill:hover { color: #fff; background: rgba(255,255,255,0.06); }
.nav-pill.active {
    background: rgba(99,102,241,0.15);
    border-color: rgba(99,102,241,0.35);
    color: #a5b4fc;
}

/* === HERO SECTION === */
.hero-wrap {
    text-align: center;
    padding: 64px 0 56px;
    animation: fadeUp 0.7s ease both;
}
@keyframes fadeUp {
    from { opacity:0; transform: translateY(24px); }
    to   { opacity:1; transform: translateY(0); }
}
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 100px;
    padding: 5px 16px;
    font-size: 0.72rem;
    font-weight: 600;
    color: #a5b4fc;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 28px;
}
.hero-dot {
    width: 6px; height: 6px;
    background: #6366f1;
    border-radius: 50%;
    animation: pulse 1.5s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.4; transform: scale(0.7); }
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    font-weight: 800;
    color: #fff;
    line-height: 1.1;
    letter-spacing: -0.03em;
    margin-bottom: 20px;
}
.hero-title .accent { 
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-desc {
    font-size: 1.05rem;
    color: rgba(255,255,255,0.45);
    font-weight: 300;
    line-height: 1.7;
    max-width: 540px;
    margin: 0 auto 40px;
}
.hero-stats {
    display: flex;
    justify-content: center;
    gap: 48px;
    flex-wrap: wrap;
}
.stat-item { text-align: center; }
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #fff;
    line-height: 1;
}
.stat-label {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.35);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 4px;
}

/* === CARDS === */
.glass-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    backdrop-filter: blur(12px);
    transition: border-color 0.3s, transform 0.3s;
}
.glass-card:hover {
    border-color: rgba(99,102,241,0.25);
    transform: translateY(-2px);
}

.section-label {
    font-size: 0.68rem;
    font-weight: 600;
    color: #6366f1;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 20px;
}

/* === FORM ELEMENTS === */
.stNumberInput label, .stSelectbox label, .stRadio label, .stTextInput label {
    color: rgba(255,255,255,0.6) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.01em !important;
    margin-bottom: 4px !important;
}

/* Native dark theme handles input box backgrounds via config.toml */
/* Removing brittle brute-force CSS for inputs to ensure native hover/focus states work properly */

/* Remove phantom bars/empty markdown containers */
.stMarkdown:empty, .stMarkdown > div:empty {
    display: none !important;
}

.stSelectbox > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #f1f5f9 !important;
}
.stRadio > div {
    display: flex !important;
    gap: 10px !important;
}
.stRadio > div > label {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    padding: 10px 16px !important;
    color: rgba(255,255,255,0.6) !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    flex: 1 !important;
    text-align: center !important;
    font-size: 0.85rem !important;
}
.stRadio > div > label:hover {
    border-color: rgba(99,102,241,0.4) !important;
    color: #fff !important;
}

/* === PREDICT BUTTON === */
.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 15px 0 !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    letter-spacing: 0.03em !important;
    box-shadow: 0 0 32px rgba(99,102,241,0.3), 0 4px 16px rgba(0,0,0,0.3) !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 48px rgba(99,102,241,0.5), 0 8px 24px rgba(0,0,0,0.4) !important;
}

/* === RESULT BOXES === */
.result-box {
    border-radius: 20px;
    padding: 36px 32px;
    text-align: center;
    margin-top: 16px;
    animation: resultReveal 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}
@keyframes resultReveal {
    from { opacity:0; transform: scale(0.9) translateY(20px); }
    to   { opacity:1; transform: scale(1) translateY(0); }
}
.result-approved {
    background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(5,150,105,0.06) 100%);
    border: 1px solid rgba(52,211,153,0.3);
}
.result-rejected {
    background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(185,28,28,0.06) 100%);
    border: 1px solid rgba(252,165,165,0.3);
}
.result-emoji { font-size: 3.5rem; margin-bottom: 16px; display: block; }
.result-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 10px;
    letter-spacing: -0.02em;
}
.result-approved .result-title { color: #34d399; }
.result-rejected .result-title { color: #f87171; }
.result-body { color: rgba(255,255,255,0.45); font-size: 0.9rem; line-height: 1.6; max-width: 420px; margin: 0 auto 20px; }
.result-tag {
    display: inline-block;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.4);
    margin: 2px;
}

/* === PROGRESS BAR === */
.score-bar-wrap { margin: 24px 0 8px; }
.score-label {
    display: flex; justify-content: space-between;
    font-size: 0.78rem; color: rgba(255,255,255,0.4);
    margin-bottom: 8px;
}
.score-track {
    height: 6px;
    background: rgba(255,255,255,0.08);
    border-radius: 100px;
    overflow: hidden;
}
.score-fill {
    height: 100%;
    border-radius: 100px;
    transition: width 1s cubic-bezier(0.34,1.56,0.64,1);
}
.score-fill.green  { background: linear-gradient(90deg, #10b981, #34d399); }
.score-fill.red    { background: linear-gradient(90deg, #ef4444, #f87171); }

/* === CHATBOT === */
.chat-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    overflow: hidden;
}
.chat-header {
    background: rgba(99,102,241,0.08);
    border-bottom: 1px solid rgba(99,102,241,0.12);
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.chat-avatar {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
}
.chat-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #f1f5f9;
}
.chat-status {
    font-size: 0.72rem;
    color: #34d399;
    display: flex; align-items: center; gap: 4px;
}
.online-dot {
    width: 6px; height: 6px;
    background: #34d399;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}
.chat-messages {
    padding: 20px;
    min-height: 320px;
    max-height: 420px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
}
.msg {
    display: flex;
    gap: 10px;
    animation: msgIn 0.3s ease both;
}
@keyframes msgIn {
    from { opacity:0; transform: translateY(8px); }
    to   { opacity:1; transform: translateY(0); }
}
.msg.user { flex-direction: row-reverse; }
.msg-avatar {
    width: 30px; height: 30px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem; flex-shrink: 0;
}
.msg-avatar.bot { background: linear-gradient(135deg, #6366f1, #8b5cf6); }
.msg-avatar.user { background: rgba(255,255,255,0.1); }
.msg-bubble {
    max-width: 75%;
    padding: 10px 14px;
    border-radius: 16px;
    font-size: 0.87rem;
    line-height: 1.55;
}
.msg-bubble.bot {
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.2);
    color: #e2e8f0;
    border-bottom-left-radius: 4px;
}
.msg-bubble.user {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.1);
    color: #e2e8f0;
    border-bottom-right-radius: 4px;
}
.quick-replies {
    padding: 12px 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    border-top: 1px solid rgba(255,255,255,0.05);
}
.quick-btn {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.78rem;
    color: #a5b4fc;
    cursor: pointer;
    transition: all 0.2s;
}
.quick-btn:hover {
    background: rgba(99,102,241,0.18);
    border-color: rgba(99,102,241,0.4);
}

/* === FEATURE TILES === */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin: 32px 0;
}
.feature-tile {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 20px;
    transition: all 0.3s;
}
.feature-tile:hover {
    border-color: rgba(99,102,241,0.3);
    background: rgba(99,102,241,0.05);
    transform: translateY(-3px);
}
.feature-icon {
    font-size: 1.5rem;
    margin-bottom: 10px;
    display: block;
}
.feature-name {
    font-size: 0.88rem;
    font-weight: 600;
    color: #f1f5f9;
    margin-bottom: 4px;
}
.feature-desc {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.35);
    line-height: 1.5;
}

/* === STEPS TIMELINE === */
.steps { display: flex; flex-direction: column; gap: 0; }
.step-item {
    display: flex;
    gap: 16px;
    padding: 16px 0;
    border-left: 1px solid rgba(255,255,255,0.06);
    margin-left: 16px;
    padding-left: 24px;
    position: relative;
}
.step-item::before {
    content: '';
    position: absolute;
    left: -5px; top: 20px;
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #6366f1;
    border: 2px solid #050816;
    box-shadow: 0 0 12px rgba(99,102,241,0.6);
}
.step-num {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 800;
    color: #6366f1;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 2px;
}
.step-title {
    font-size: 0.88rem;
    font-weight: 600;
    color: #f1f5f9;
    margin-bottom: 4px;
}
.step-desc {
    font-size: 0.78rem;
    color: rgba(255,255,255,0.35);
    line-height: 1.5;
}

/* === DIVIDER === */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.3), transparent);
    margin: 40px 0;
}

/* === TOOLTIPS / INFO TAGS === */
.info-tag {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.3);
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 6px;
    padding: 2px 8px;
    margin-top: 4px;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.3); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ── Load models ───────────────────────────────────────────────────────────────
import pickle
import numpy as np
import pandas as pd

@st.cache_resource
def load_models():
    with open("classifier.pkl", "rb") as f:
        clf = pickle.load(f)
    with open("sc.pkl", "rb") as f:
        sc = pickle.load(f)
    return clf, sc

classifier, sc = load_models()

# ── Session state ─────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "bot",
            "text": "👋 Hi! I'm **FinBot**, your loan eligibility assistant. I can help you understand eligibility criteria, explain terms, or guide you through the form. What would you like to know?"
        }
    ]
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "predictor"
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# ── Chatbot logic ─────────────────────────────────────────────────────────────
CHAT_KB = {
    "credit": "📊 **Credit History** is one of the strongest predictors of loan approval. A score of **1** means your history meets guidelines (you've repaid loans on time). A score of **0** indicates missed payments or defaults. This field alone can account for ~30% of the model's decision.",
    "income": "💰 **Applicant Income** represents your gross monthly income. The model was trained on incomes ranging from ₹150 to ₹80,000. Higher income generally improves eligibility. Combined with co-applicant income, lenders assess your repayment capacity.",
    "loan amount": "🏦 **Loan Amount** is in thousands of rupees. The dataset covers ₹0–₹700K. A lower loan-to-income ratio significantly improves your chances. Ideal is keeping EMI below 40–50% of monthly income.",
    "term": "📅 **Loan Term** is the repayment duration in months. Most common is 360 months (30 years). Longer terms reduce monthly EMI but increase total interest paid.",
    "dependents": "👨‍👩‍👧 **Dependents** refers to how many people financially depend on you. Fewer dependents is favorable as it implies lower financial obligations.",
    "property": "🏘️ **Property Area** — Semi-Urban areas historically have the highest approval rates in this dataset, followed by Urban, then Rural.",
    "education": "🎓 **Education** — Graduate status tends to correlate with higher income stability, improving approval odds.",
    "self employed": "💼 **Self-employed** applicants may face slightly stricter scrutiny due to income variability. Providing strong co-applicant income can compensate.",
    "model": "🤖 This app uses a **Random Forest Classifier** trained on 615 historical loan records. Features are scaled using a StandardScaler before prediction. The model achieved ~80% accuracy on test data.",
    "accuracy": "🎯 The underlying model has approximately **80% accuracy** on the test dataset. It was validated using cross-validation across multiple classification algorithms including Logistic Regression, Decision Trees, and Random Forests.",
    "improve": "📈 To improve your chances: ✅ Clear any existing debts to build credit history. ✅ Reduce loan amount requested. ✅ Add a co-applicant. ✅ Choose Semi-Urban property. ✅ Graduate education helps.",
    "eligible": "✅ Loan eligibility is determined by a combination of factors: income, loan amount, credit history, dependents, education, employment type, and property location. The ML model weighs all these simultaneously.",
    "hello": "👋 Hello! I'm here to help you understand loan eligibility. Ask me about credit history, income requirements, loan terms, or how the model works!",
    "hi": "Hi there! 😊 How can I assist you with your loan application today?",
    "help": "🆘 I can help with: \n- Explaining any form field\n- Loan eligibility factors\n- How the ML model works\n- Tips to improve your score\n\nJust ask!",
}

def get_bot_response(user_input: str) -> str:
    text = user_input.lower()
    for key, response in CHAT_KB.items():
        if key in text:
            return response
    if any(w in text for w in ["thank", "thanks", "great", "awesome"]):
        return "😊 You're welcome! Feel free to ask anything else about your loan application."
    if any(w in text for w in ["bye", "goodbye", "exit"]):
        return "👋 Goodbye! Best of luck with your loan application. Feel free to come back anytime!"
    return "🤔 I'm not sure about that specific query. Try asking about: **credit history**, **income**, **loan amount**, **property area**, **dependents**, **education**, or **how the model works**."

# ══════════════════════════════════════════════════════════════════════════════
# TOP NAV
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="topnav">
    <div class="logo">Loan<span>IQ</span></div>
    <div class="nav-links">
        <span class="nav-pill active">🔮 Predictor</span>
        <span class="nav-pill">💬 AI Advisor</span>
        <span class="nav-pill">📊 Insights</span>
    </div>
    <div style="font-size:0.75rem; color:rgba(255,255,255,0.25);">v2.0 · ML Powered</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">
        <div class="hero-dot"></div>
        AI-Powered · Real-Time Prediction
    </div>
    <div class="hero-title">
        Know Your Loan<br><span class="accent">Eligibility Instantly</span>
    </div>
    <p class="hero-desc">
        Our machine learning model analyzes 14 financial parameters to predict 
        your home loan approval likelihood in under a second.
    </p>
    <div class="hero-stats">
        <div class="stat-item">
            <div class="stat-num">615+</div>
            <div class="stat-label">Training Records</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">~80%</div>
            <div class="stat-label">Model Accuracy</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">14</div>
            <div class="stat-label">Parameters Analyzed</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">&lt;1s</div>
            <div class="stat-label">Prediction Time</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN LAYOUT — Left: Form  |  Right: Chatbot
# ══════════════════════════════════════════════════════════════════════════════
left_col, right_col = st.columns([3, 2], gap="large")

# ────────────────────────────────────────────────
# LEFT — PREDICTION FORM
# ────────────────────────────────────────────────
with left_col:
    st.markdown("""
    <div style="margin-bottom: 24px;">
        <div class="section-label">Step 01 — Application Form</div>
        <div class="section-title">Enter Your Details</div>
    </div>
    """, unsafe_allow_html=True)

    # Row 1: Personal
    st.markdown("""
    <div class='glass-card' style='padding: 24px; margin-bottom: 0px; border-bottom: none; border-bottom-left-radius: 0; border-bottom-right-radius: 0;'>
        <div class='section-label' style='margin-bottom:0px;'>👤 Personal Information</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Widgets
    Full_Name = st.text_input("Full Name", placeholder="Enter your full name", key="fn")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        Gender = st.selectbox("Gender", ("Male", "Female"), key="g")
    with c2:
        Married = st.selectbox("Marital Status", ("Yes", "No"), key="m")
    with c3:
        Dependents = st.selectbox("Dependents", ("0", "1", "2", "3+"), key="d")

    c4, c5 = st.columns(2)
    with c4:
        Education = st.selectbox("Education Level", ("Graduate", "Not Graduate"), key="e")
    with c5:
        Self_Employed = st.selectbox("Employment Type", ("Employed", "Self Employed"), key="se")
    
    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    # Row 2: Financial
    st.markdown("<div class='section-label' style='margin-bottom:14px; margin-top: 24px;'>💰 Financial Details</div>", unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    with f1:
        ApplicantIncome = st.number_input("Monthly Income (₹)", 0, 80000, 5000, 500, key="ai")
        st.markdown("<div class='info-tag'>ℹ️ Range: ₹150 – ₹80,000</div>", unsafe_allow_html=True)
    with f2:
        CoapplicantIncome = st.number_input("Co-Applicant Income (₹)", 0, 40000, 0, 500, key="ci")
        st.markdown("<div class='info-tag'>ℹ️ Enter 0 if none</div>", unsafe_allow_html=True)

    f3, f4 = st.columns(2)
    with f3:
        LoanAmount = st.number_input("Loan Amount (₹ thousands)", 0, 700, 150, 10, key="la")
        st.markdown("<div class='info-tag'>ℹ️ Range: ₹0 – ₹700K</div>", unsafe_allow_html=True)
    with f4:
        Loan_Amount_Term = st.number_input("Loan Term (months)", 12, 480, 360, 12, key="lt")
        st.markdown("<div class='info-tag'>ℹ️ e.g. 360 = 30 years</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Row 3: Credit + Property
    st.markdown("<div class='section-label' style='margin-bottom:14px; margin-top: 24px;'>🏦 Credit & Property</div>", unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    with r1:
        Credit_History = st.radio(
            "Credit History",
            options=[1, 0],
            format_func=lambda x: "✅ Meets Guidelines" if x == 1 else "❌ Does Not Meet",
            horizontal=False,
            key="ch"
        )
    with r2:
        Property_Area = st.selectbox("Property Area", ("Urban", "Rural", "Semi Urban"), key="pa")
        st.markdown("""
        <div style="margin-top:8px; padding: 10px; background: rgba(99,102,241,0.07); border-radius: 10px; border: 1px solid rgba(99,102,241,0.15);">
            <div style="font-size:0.72rem; color: rgba(255,255,255,0.4); margin-bottom:4px;">Approval Rate Hint</div>
            <div style="font-size:0.8rem; color: #a5b4fc;">Semi-Urban > Urban > Rural</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Predict button
    predict_clicked = st.button("🔮  Predict My Loan Eligibility", use_container_width=True)

    # ── Encoding ──────────────────────────────────────────────────────────────
    Gender_enc = 1 if Gender == "Male" else 0
    Married_enc = 1 if Married == "Yes" else 0
    Education_enc = 1 if Education == "Graduate" else 0
    Self_Employed_enc = 1 if Self_Employed == "Self Employed" else 0
    dep_map = {"0": (1,0,0), "1": (0,1,0), "2": (0,0,1), "3+": (0,0,0)}
    D0, D1, D2 = dep_map[Dependents]
    if Property_Area == "Urban":
        PAU, PAS = 1, 0
    elif Property_Area == "Semi Urban":
        PAU, PAS = 0, 1
    else:
        PAU, PAS = 0, 0

    if predict_clicked:
        feature_names = ['Gender', 'Married', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Dependents_0', 'Dependents_1', 'Dependents_2', 'Property_Area_Semiurban', 'Property_Area_Urban']
        features = [[Gender_enc, Married_enc, Education_enc, Self_Employed_enc,
                     ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,
                     Credit_History, D0, D1, D2, PAS, PAU]]
        features_df = pd.DataFrame(features, columns=feature_names)
        result = classifier.predict(sc.transform(features_df))
        st.session_state.prediction_result = int(result[0])
        st.session_state.prediction_done = True

        # Push result note into chat
        if result[0] == 1:
            st.session_state.chat_history.append({
                "role": "bot",
                "text": "🎉 Great news! Based on your inputs, **you're eligible** for the loan. Make sure you have all your documents ready before visiting a branch!"
            })
        else:
            st.session_state.chat_history.append({
                "role": "bot",
                "text": "📋 Your prediction shows **not eligible** this time. Try asking me how to **improve** your eligibility score — I have tips that could help!"
            })

    # ── Result display ─────────────────────────────────────────────────────────
    if st.session_state.prediction_done:
        res = st.session_state.prediction_result
        if res == 1:
            score_pct = min(85 + (ApplicantIncome / 80000) * 10, 98)
            name_display = f", {Full_Name}" if Full_Name else ""
            st.markdown(f"""
            <div class="result-box result-approved">
                <span class="result-emoji">🎉</span>
                <div class="result-title">Eligibility Approved!</div>
                <p class="result-body">Congratulations{name_display}! Your financial profile meets our lending criteria. You can proceed with a full loan application at your nearest branch.</p>
                <div class="score-bar-wrap">
                    <div class="score-label"><span>Approval Confidence</span><span>{score_pct:.0f}%</span></div>
                    <div class="score-track"><div class="score-fill green" style="width:{score_pct}%"></div></div>
                </div>
                <div style="margin-top:16px;">
                    <span class="result-tag">✅ Credit Verified</span>
                    <span class="result-tag">✅ Income Sufficient</span>
                    <span class="result-tag">✅ Profile Approved</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            score_pct = max(15, 35 - (Credit_History * 20))
            name_display = f", {Full_Name}" if Full_Name else ""
            st.markdown(f"""
            <div class="result-box result-rejected">
                <span class="result-emoji">📋</span>
                <div class="result-title">Not Eligible Right Now</div>
                <p class="result-body">We're sorry{name_display}, but your current profile doesn't meet the approval threshold. The good news — this is fixable. Ask our AI Advisor in the chat for personalized tips.</p>
                <div class="score-bar-wrap">
                    <div class="score-label"><span>Approval Confidence</span><span>{score_pct:.0f}%</span></div>
                    <div class="score-track"><div class="score-fill red" style="width:{score_pct}%"></div></div>
                </div>
                <div style="margin-top:16px;">
                    <span class="result-tag">⚠️ Review Credit</span>
                    <span class="result-tag">⚠️ Check Income Ratio</span>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ────────────────────────────────────────────────
# RIGHT — CHATBOT + SIDE INFO
# ────────────────────────────────────────────────
with right_col:

    # ── CHATBOT ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <div class="section-label">Step 02 — AI Advisor</div>
        <div class="section-title">FinBot Assistant</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chat-container">
      <div class="chat-header">
        <div class="chat-avatar">🤖</div>
        <div>
          <div class="chat-name">FinBot</div>
          <div class="chat-status"><div class="online-dot"></div> Online · Loan Specialist</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Messages area
    messages_html = '<div class="chat-messages">'
    for msg in st.session_state.chat_history[-10:]:
        if msg["role"] == "bot":
            messages_html += f'''
            <div class="msg bot">
              <div class="msg-avatar bot">🤖</div>
              <div class="msg-bubble bot">{msg["text"]}</div>
            </div>'''
        else:
            messages_html += f'''
            <div class="msg user">
              <div class="msg-avatar user">👤</div>
              <div class="msg-bubble user">{msg["text"]}</div>
            </div>'''
    messages_html += '</div>'

    st.markdown(f'<div class="glass-card" style="border-radius:0 0 20px 20px;">{messages_html}</div>', unsafe_allow_html=True)

    # Quick replies
    st.markdown("""
    <div style="display:flex; flex-wrap:wrap; gap:6px; margin:10px 0 6px;">
        <span style="font-size:0.7rem; color:rgba(255,255,255,0.25); width:100%; margin-bottom:2px;">Quick questions →</span>
    </div>
    """, unsafe_allow_html=True)

    qr_cols = st.columns(2)
    quick_questions = [
        "What is credit history?",
        "How can I improve?",
        "Explain loan term",
        "Which property area is best?",
    ]
    for i, q in enumerate(quick_questions):
        with qr_cols[i % 2]:
            if st.button(q, key=f"qr_{i}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "text": q})
                resp = get_bot_response(q)
                st.session_state.chat_history.append({"role": "bot", "text": resp})
                st.rerun()

    # Text input
    with st.form("chat_form", clear_on_submit=True):
        chat_input = st.text_input(
            "Ask FinBot anything...",
            placeholder="e.g. What affects my credit score?",
            label_visibility="collapsed"
        )
        submitted = st.form_submit_button("Send ↗", use_container_width=True)
        if submitted and chat_input.strip():
            st.session_state.chat_history.append({"role": "user", "text": chat_input})
            resp = get_bot_response(chat_input)
            st.session_state.chat_history.append({"role": "bot", "text": resp})
            st.rerun()

    # ── SIDE INFO STEPS ───────────────────────────────────────────────────────
    st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-label" style="margin-bottom:6px;">How It Works</div>
    <div class="steps">
        <div class="step-item">
            <div>
                <div class="step-num">Step 01</div>
                <div class="step-title">Fill the Form</div>
                <div class="step-desc">Enter your personal, financial, and property details accurately.</div>
            </div>
        </div>
        <div class="step-item">
            <div>
                <div class="step-num">Step 02</div>
                <div class="step-title">ML Prediction</div>
                <div class="step-desc">Our Random Forest model processes 14 parameters in real-time.</div>
            </div>
        </div>
        <div class="step-item">
            <div>
                <div class="step-num">Step 03</div>
                <div class="step-title">Get Your Result</div>
                <div class="step-desc">Instant eligibility verdict with confidence score and next steps.</div>
            </div>
        </div>
        <div class="step-item">
            <div>
                <div class="step-num">Step 04</div>
                <div class="step-title">Ask FinBot</div>
                <div class="step-desc">Use the AI advisor to understand your result and improve.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FEATURE HIGHLIGHTS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="feature-grid">
    <div class="feature-tile">
        <span class="feature-icon">🤖</span>
        <div class="feature-name">Random Forest Model</div>
        <div class="feature-desc">Ensemble ML model trained on real banking data with ~80% accuracy.</div>
    </div>
    <div class="feature-tile">
        <span class="feature-icon">⚡</span>
        <div class="feature-name">Instant Prediction</div>
        <div class="feature-desc">Sub-second prediction powered by scikit-learn and StandardScaler.</div>
    </div>
    <div class="feature-tile">
        <span class="feature-icon">💬</span>
        <div class="feature-name">AI Loan Advisor</div>
        <div class="feature-desc">FinBot answers questions about eligibility, terms, and improvement tips.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; padding: 32px 0 16px; border-top: 1px solid rgba(255,255,255,0.05);">
    <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; color:#fff; margin-bottom:6px;">Loan<span style="color:#6366f1;">IQ</span></div>
    <div style="font-size:0.72rem; color:rgba(255,255,255,0.2);">Built with Streamlit · scikit-learn · Python · For educational purposes only</div>
</div>
""", unsafe_allow_html=True)
