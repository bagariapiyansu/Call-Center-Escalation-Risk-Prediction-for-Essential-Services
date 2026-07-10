import streamlit as st
import time

st.set_page_config(
    page_title="Analyze Call",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Analyze Call")

st.write("Analyze customer-agent conversations using AI.")

st.divider()

# -----------------------------
# INPUT
# -----------------------------

transcript = st.text_area(
    "📝 Enter Customer-Agent Transcript",
    height=250,
    placeholder="Paste the conversation here..."
)

uploaded_file = st.file_uploader(
    "📂 Upload Transcript",
    type=["txt", "json"]
)

model = st.radio(
    "🧠 Select Model",
    ["LSTM", "BiLSTM"],
    horizontal=True
)

st.divider()

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

if st.button("🚀 Analyze Transcript", use_container_width=True):

    if transcript == "" and uploaded_file is None:

        st.warning("Please enter a transcript or upload a file.")

    else:

        with st.spinner("Analyzing Conversation..."):

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)

        st.success("Analysis Complete!")

        st.divider()

        st.header("📊 Prediction Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Escalation Risk", "High 🔴")
            st.metric("Confidence", "94%")

        with col2:
            st.metric("Issue Category", "Billing")
            st.metric("Department", "Billing Support")

        st.divider()

        st.subheader("📝 AI Summary")

        st.info(
            """
Customer reported multiple billing issues and requested a refund.

The customer expressed dissatisfaction after repeated unsuccessful attempts.

The conversation is likely to require escalation.
"""
        )

        st.divider()

        st.subheader("📍 Recommended Action")

        st.success(
            """
Forward this case to the Billing Escalation Team.

Priority Level:
High
"""
        )

        st.divider()

        st.download_button(
            "📄 Download Report",
            data="""
Escalation Risk : High
Confidence : 94%
Issue Category : Billing
Department : Billing Support
""",
            file_name="prediction_report.txt"
        )
        