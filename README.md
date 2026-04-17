# 💎 LoanIQ — Smart Loan Eligibility Predictor

A professional, AI-powered loan eligibility web app built with Streamlit.

## ✨ Features
- 🔮 ML-powered eligibility prediction (Random Forest)
- 💬 FinBot AI chatbot advisor
- 🎨 Modern dark UI with animations
- 📊 Confidence score visualization
- ⚡ Real-time prediction

## 🚀 Quick Start (Local)

### 1. Prerequisites
- Python 3.9 or higher
- pip

### 2. Setup virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 📁 Project Structure
```
loaniq/
├── app.py              # Main Streamlit application
├── classifier.pkl      # Trained Random Forest model
├── sc.pkl              # StandardScaler for feature scaling
├── requirements.txt    # Python dependencies
├── Procfile            # Heroku/Render deployment
├── setup.sh            # Streamlit server config
└── README.md           # This file
```

## 🌐 Deploy to Streamlit Cloud (Free)

1. Push this folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file as `app.py`
5. Click **Deploy** ✅

## 🌐 Deploy to Render (Free)

1. Push to GitHub
2. Create new **Web Service** on [render.com](https://render.com)
3. Build command: `pip install -r requirements.txt`
4. Start command: `sh setup.sh && streamlit run app.py`

---

## 📊 Model Info
- **Algorithm**: Random Forest Classifier
- **Training Data**: 615 loan records
- **Features**: 14 (gender, income, credit history, etc.)
- **Accuracy**: ~80%
- **Scaler**: StandardScaler

## 🤖 FinBot Topics
Ask FinBot about:
- Credit history
- Income requirements
- Loan amount & terms
- Property area impact
- How to improve eligibility
- Model accuracy

---
*Built for educational purposes. Not financial advice.*
