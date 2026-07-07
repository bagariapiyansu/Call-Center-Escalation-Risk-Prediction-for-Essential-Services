import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Analyze Call",
    page_icon="📞",
    layout="wide"
)

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------
st.title("📞 Analyze Customer Conversation")

st.caption("AI-Powered Escalation Risk Prediction System")

st.divider()

# --------------------------------------------------
# INSTRUCTIONS
# --------------------------------------------------
st.info(
    """
Paste a customer-agent conversation or upload a transcript file.

The AI model will analyze the conversation and provide:

• 🚨 Escalation Risk

• 📂 Issue Category

• 📝 Conversation Summary

• 📍 Routing Recommendation
"""
)

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
col1, col2 = st.columns([3, 1])

# Left Column
with col1:

    transcript = st.text_area(
        "📝 Customer-Agent Transcript",
        height=350,
        placeholder="""
Example:

Customer: I have called three times regarding my refund.
Agent: I'm sorry for the inconvenience. Let me check your account.
Customer: This issue is still unresolved and I want to speak with your supervisor.
"""
    )

# Right Column
with col2:

    st.subheader("📂 Upload File")

    uploaded_file = st.file_uploader(
        "Choose Transcript",
        type=["txt", "json"]
    )

    st.divider()

    st.subheader("🤖 AI Model")

    st.success("🟢 Connected")

    st.write("**Current Model**")

    st.info("BiLSTM")

    st.divider()

    st.subheader("📄 Supported Formats")

    st.write("✅ TXT")

    st.write("✅ JSON")

    st.divider()

    st.subheader("💡 Tips")

    st.caption(
        """
• Upload a complete conversation.

• Use English transcripts.

• Ensure the transcript is readable.

• Larger transcripts may take longer to analyze.
"""
    )

st.divider()

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------
analyze = st.button(
    "🚀 Analyze Conversation",
    use_container_width=True
)