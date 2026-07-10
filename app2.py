import streamlit as st
import time



# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Call Center Escalation Risk Prediction",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOADING SCREEN (Runs Once)
# --------------------------------------------------
if "loaded" not in st.session_state:
    with st.spinner("🔄 Loading AI Model..."):
        time.sleep(2)

    st.toast("✅ Model Loaded Successfully!")
    st.session_state.loaded = True

# --------------------------------------------------
# WELCOME POPUP (Runs Once)
# --------------------------------------------------
@st.dialog("👋 Welcome")
def welcome_dialog():

    st.markdown("""
# 📞 Call Center Escalation Risk Prediction

### AI-Powered Decision Support System

Welcome to the **Call Center Escalation Risk Prediction System**.

This application helps call centers:

- ✅ Predict Escalation Risk
- ✅ Classify Customer Issues
- ✅ Generate Conversation Summary
- ✅ Recommend Routing Department
- ✅ Support Faster Decision Making

---

Click **Start Application** to continue.
""")

    if st.button("🚀 Start Application", use_container_width=True):
        st.session_state.show_popup = False
        st.rerun()

if "show_popup" not in st.session_state:
    st.session_state.show_popup = True

if st.session_state.show_popup:
    welcome_dialog()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.title("📞 Navigation")

    st.success("Use the pages below")

    st.divider()

    st.subheader("📂 Pages")

    st.write("🏠 Home")
    st.write("📞 Analyze Call")
    st.write("📁 Batch Analysis")
    st.write("📊 Dashboard")
    st.write("ℹ About")

    st.divider()

    st.subheader("⚙ Project")

    st.write("**Model**")
    st.write("LSTM / BiLSTM")

    st.write("**Framework**")
    st.write("Streamlit")

    st.write("**Dataset**")
    st.write("CallCenterEN (61K Conversations)")

    st.divider()

    st.caption("Version 1.0")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.title("📞 Call Center Escalation Risk Prediction")

st.caption("AI-Powered Decision Support System for Essential Services")

st.divider()

st.info("""
Analyze customer-agent conversations using Artificial Intelligence.

The application predicts whether a conversation is likely to require escalation,
helps identify the issue category, generates a summary,
and recommends the appropriate department.
""")

# --------------------------------------------------
# PROJECT FEATURES
# --------------------------------------------------
st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("Analyze Individual Transcript")
    st.success("Escalation Risk Prediction")
    st.success("Issue Category Detection")
    st.success("Conversation Summary")

with col2:
    st.success("Routing Recommendation")
    st.success("Batch CSV Analysis")
    st.success("Interactive Dashboard")
    st.success("Download Prediction Results")

st.divider()

# --------------------------------------------------
# SYSTEM WORKFLOW
# --------------------------------------------------
st.header("⚙ System Workflow")

st.code("""
Customer Call
      │
      ▼
Speech → Transcript
      │
      ▼
Text Cleaning
      │
      ▼
Tokenization
      │
      ▼
LSTM / BiLSTM
      │
      ▼
Escalation Prediction
      │
      ▼
Conversation Summary
      │
      ▼
Routing Recommendation
""")

st.divider()

# --------------------------------------------------
# AI MODEL
# --------------------------------------------------
st.header("🤖 AI Model")

st.subheader("Current Model")

st.write("✅ LSTM")
st.write("✅ BiLSTM")

st.divider()

st.subheader("Future Improvements")

st.write("🔹 BERT")
st.write("🔹 RoBERTa")
st.write("🔹 DistilBERT")
st.write("🔹 Explainable AI (SHAP)")

st.divider()

# --------------------------------------------------
# PROJECT STATISTICS
# --------------------------------------------------
# st.header("📊 Project Statistics")

# st.metric("Dataset", "61K+ Conversations")
# st.metric("Language", "English")
# st.metric("Domains", "Healthcare, Insurance, Automotive, Customer Service")
# st.metric("Prediction", "Low • Medium • High")

# --------------------------------------------------
# PROJECT STATISTICS
# --------------------------------------------------

# st.header("📊 Project Statistics")
# st.metric("📂 Dataset", "61K+ Conversations")
# st.metric("🌐 Language", "English")
# st.metric("🏢 Domains", "4 Major Domains")

# st.write("""
# • 🏥 Healthcare
# • 🛡️ Insurance
# • 🚗 Automotive
# • 📞 Customer Service
# """)

# st.subheader("🎯 Prediction Levels")
# st.success("🟢 Low Risk")
# st.warning("🟡 Medium Risk")
# st.error("🔴 High Risk")
# st.divider()
# st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📂 Dataset", "61K+")

with col2:
    st.metric("🌐 Language", "English")

with col3:
    st.metric("🏢 Domains", "4")

st.subheader("🏢 Supported Domains")
st.write("• 🏥 Healthcare")
st.write("• 🛡️ Insurance")
st.write("• 🚗 Automotive")
st.write("• 📞 Customer Service")

st.subheader("🎯 Escalation Risk Levels")
st.success("🟢 Low Risk")
st.warning("🟡 Medium Risk")
st.error("🔴 High Risk")



# --------------------------------------------------
# QUICK START
# --------------------------------------------------
st.header("🚀 Quick Start")

st.write("""
1. Open **Analyze Call** from the sidebar.
2. Paste a customer-agent transcript.
3. Click **Analyze**.
4. View:
   - Escalation Risk
   - Issue Category
   - Summary
   - Recommended Department
""")

if st.button("🚀 Go to Analyze Call", use_container_width=True):
    st.success("Open the 'Analyze Call' page from the sidebar.")

st.divider()

# --------------------------------------------------
# # FOOTER  OPTION 1
# # --------------------------------------------------
# st.markdown(
# """
# <center>

# ### 📞 Call Center Escalation Risk Prediction

# Developed using **•Python 
# • Streamlit 
# • TensorFlow 
# • Scikit-learn**


# </center>
# """,
# unsafe_allow_html=True
# )


# --------------------------------------------------
# # FOOTER  OPTION 2
# # --------------------------------------------------

# st.markdown("---")

# st.subheader("🛠 Developed Using")

# st.success("🐍 Python")

# st.info("🌐 Streamlit")

# st.warning("🧠 TensorFlow")

# st.success("📊 Scikit-learn")

# st.markdown("---")

# st.caption("📞 Call Center Escalation Risk Prediction ")



# --------------------------------------------------
# # FOOTER  OPTION 3 
# # --------------------------------------------------

st.markdown("---")

st.markdown(
"""
<center>

## 📞 Call Center Escalation Risk Prediction

### Developed using

🐍 **Python**

🌐 **Streamlit**

🧠 **TensorFlow**

📊 **Scikit-learn**

---
</center>
""",
unsafe_allow_html=True
)
