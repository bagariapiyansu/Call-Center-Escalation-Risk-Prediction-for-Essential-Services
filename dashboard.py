import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_option_menu import option_menu

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="SmartCall AI Dashboard",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#183153;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
    text-align:center;
}

.banner{
    background:linear-gradient(90deg,#2563eb,#3b82f6);
    padding:30px;
    border-radius:18px;
    color:white;
}

.banner h2{
    color:white;
}

div[data-testid="stMetric"]{
    background:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0 3px 10px rgba(0,0,0,.08);
}

section[data-testid="stSidebar"]{
    background:#183153;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=80
    )

    st.title("SmartCall AI")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Dashboard",
            "Analyze Call",
            "Dataset",
            "Analytics",
            "History",
            "Agent Performance",
            "Reports",
            "Settings",
            "About"
        ],
        icons=[
            "house",
            "telephone",
            "database",
            "bar-chart",
            "clock-history",
            "people",
            "file-earmark-text",
            "gear",
            "info-circle"
        ],
        default_index=0,
    )

    st.divider()

    st.success("🟢 AI Model Connected")

    st.caption("Model Version")
    st.info("BiLSTM v1.0")

    st.divider()

    st.write("System Status")

    st.progress(100)

    st.success("Running")

# -------------------------------------------------
# HEADER
# -------------------------------------------------

left, right = st.columns([4,1])

with left:

    st.title("📞 SmartCall AI Dashboard")

    st.caption(
        "AI Powered Call Center Escalation Risk Prediction System"
    )

with right:

    st.metric(
        "Today's Date",
        datetime.now().strftime("%d-%m-%Y")
    )

st.divider()

# -------------------------------------------------
# WELCOME BANNER
# -------------------------------------------------

st.markdown("""

<div class="banner">

<h2>👋 Welcome Back!</h2>

Monitor customer conversations, analyze escalation risks,
track agent performance, and gain actionable insights through
AI-powered analytics.

</div>

""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# DUMMY KPI VALUES
# -------------------------------------------------

total_calls = 15234
high_risk = 742
resolved = 13950
avg_sentiment = 84

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(
        "📞 Total Calls",
        f"{total_calls:,}",
        "+8%"
    )

with col2:

    st.metric(
        "🚨 High Risk Calls",
        high_risk,
        "-3%"
    )

with col3:

    st.metric(
        "😊 Avg Sentiment",
        f"{avg_sentiment}%",
        "+4%"
    )

with col4:

    resolution_rate = round((resolved/total_calls)*100,2)

    st.metric(
        "✔ Resolution Rate",
        f"{resolution_rate}%",
        "+2%"
    )

st.write("")

# -------------------------------------------------
# QUICK SUMMARY
# -------------------------------------------------

left,right = st.columns([2,1])

with left:

    st.subheader("📌 Dashboard Overview")

    st.write("""
This dashboard provides a centralized overview of call center
operations. Monitor customer interactions, identify escalation
risks, evaluate sentiment, and track agent performance in real time.

Use the navigation menu on the left to access:
- 📞 Analyze Call
- 📂 Dataset
- 📊 Analytics
- 📜 History
- 👨‍💼 Agent Performance
- 📄 Reports
""")

with right:

    st.info("""
### 🤖 AI Highlights

✔ Real-Time Prediction

✔ Sentiment Analysis

✔ Escalation Detection

✔ Complaint Categorization

✔ Agent Performance

✔ AI Recommendations
""")

st.divider()

st.info("📊 Charts, recent calls, complaint categories")

# =====================================================
# PART 2 - CHARTS & ANALYTICS
# =====================================================

import plotly.graph_objects as go
import numpy as np

# -----------------------------
# Dummy Data
# -----------------------------

daily_calls = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Calls": [210, 260, 240, 310, 360, 280, 190]
})

risk_df = pd.DataFrame({
    "Risk": ["Low", "Medium", "High"],
    "Count": [820, 420, 165]
})

complaints = pd.DataFrame({
    "Category": [
        "Billing",
        "Refund",
        "Delivery",
        "Technical",
        "Account"
    ],
    "Cases": [180, 145, 120, 95, 70]
})

weekly = pd.DataFrame({
    "Week": [
        "Week 1",
        "Week 2",
        "Week 3",
        "Week 4"
    ],
    "Calls": [1250, 1420, 1680, 1890]
})

# =====================================================
# CHARTS
# =====================================================

st.subheader("📊 AI Analytics Dashboard")

left, right = st.columns(2)

# -----------------------------
# Daily Calls
# -----------------------------

with left:

    fig = px.line(
        daily_calls,
        x="Day",
        y="Calls",
        markers=True,
        title="📈 Daily Call Volume"
    )

    fig.update_layout(height=380)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------
# Risk Distribution
# -----------------------------

with right:

    fig = px.pie(
        risk_df,
        names="Risk",
        values="Count",
        hole=.55,
        title="🚨 Escalation Risk Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")

# =====================================================
# SECOND ROW
# =====================================================

left, right = st.columns(2)

with left:

    fig = px.bar(
        complaints,
        x="Category",
        y="Cases",
        text_auto=True,
        title="🔥 Top Complaint Categories"
    )

    fig.update_layout(height=400)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.area(
        weekly,
        x="Week",
        y="Calls",
        title="📅 Weekly Call Volume"
    )

    fig.update_layout(height=400)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# =====================================================
# RECENT CALLS
# =====================================================

st.subheader("📋 Recent Customer Calls")

recent = pd.DataFrame({

    "Call ID":[
        "C1001",
        "C1002",
        "C1003",
        "C1004",
        "C1005"
    ],

    "Customer":[
        "John",
        "Emma",
        "Michael",
        "Sophia",
        "David"
    ],

    "Risk":[
        "High",
        "Medium",
        "Low",
        "High",
        "Low"
    ],

    "Sentiment":[
        "Negative",
        "Neutral",
        "Positive",
        "Negative",
        "Positive"
    ],

    "Status":[
        "Escalated",
        "Pending",
        "Resolved",
        "Escalated",
        "Resolved"
    ]
})

st.dataframe(
    recent,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# QUICK ACTIONS
# =====================================================

st.subheader("🚀 Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button(
        "📞 Analyze Call",
        use_container_width=True
    )

with c2:
    st.button(
        "📂 Upload Dataset",
        use_container_width=True
    )

with c3:
    st.button(
        "📊 View Analytics",
        use_container_width=True
    )

with c4:
    st.button(
        "📄 Generate Report",
        use_container_width=True
    )

st.write("")

st.success("✅ Dashboard analytics loaded successfully.")


# =====================================================
# PART 3 - AI INSIGHTS & SYSTEM MONITOR
# =====================================================

import plotly.graph_objects as go

st.divider()

st.subheader("🤖 AI Insights & System Monitor")

# =====================================================
# AI GAUGE
# =====================================================

left, right = st.columns([1.2, 1])

with left:

    gauge = go.Figure(go.Indicator(

        mode="gauge+number",

        value=84,

        title={'text':"Average Customer Satisfaction"},

        gauge={

            'axis':{'range':[0,100]},

            'bar':{'color':'green'},

            'steps':[

                {'range':[0,40],'color':'#ffcccc'},

                {'range':[40,70],'color':'#ffe6b3'},

                {'range':[70,100],'color':'#d9fdd3'}

            ]

        }

    ))

    gauge.update_layout(height=350)

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

# =====================================================
# TOP AGENTS
# =====================================================

with right:

    st.subheader("🏆 Top Performing Agents")

    agents = pd.DataFrame({

        "Agent":[
            "Emma",
            "John",
            "Sophia",
            "David",
            "Olivia"
        ],

        "Calls":[
            245,
            232,
            221,
            214,
            205
        ],

        "Resolution %":[
            98,
            97,
            95,
            94,
            93
        ],

        "Rating":[
            "⭐⭐⭐⭐⭐",
            "⭐⭐⭐⭐⭐",
            "⭐⭐⭐⭐",
            "⭐⭐⭐⭐",
            "⭐⭐⭐⭐"
        ]

    })

    st.dataframe(
        agents,
        hide_index=True,
        use_container_width=True
    )

st.divider()

# =====================================================
# ALERTS
# =====================================================

col1,col2 = st.columns(2)

with col1:

    st.subheader("🔔 AI Alerts")

    st.error("🚨 12 High-Risk Calls Detected")

    st.warning("⚠ Refund complaints increased by 18%")

    st.warning("⚠ 5 customers requested supervisors")

    st.success("✅ AI Prediction Service Running")

    st.success("✅ Database Connected")

with col2:

    st.subheader("⚙️ System Health")

    st.write("CPU Usage")

    st.progress(82)

    st.write("Memory Usage")

    st.progress(61)

    st.write("Database")

    st.success("🟢 Online")

    st.write("Prediction Model")

    st.success("🟢 Healthy")

st.divider()

# =====================================================
# LIVE ACTIVITY
# =====================================================

left,right = st.columns(2)

with left:

    st.subheader("📈 Live Activity")

    activity = pd.DataFrame({

        "Time":[

            "11:35",

            "11:28",

            "11:20",

            "11:10",

            "10:55"

        ],

        "Activity":[

            "Prediction Generated",

            "Dataset Updated",

            "Report Downloaded",

            "High Risk Call Detected",

            "Dashboard Login"

        ]

    })

    st.dataframe(
        activity,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.subheader("📌 AI Recommendations")

    st.info("""
✔ Prioritize High-Risk Calls

✔ Improve Refund Resolution

✔ Route Billing Issues to Senior Agents

✔ Monitor Repeat Customers

✔ Schedule Follow-up Calls

✔ Review Agent Performance Weekly
""")

st.divider()

# =====================================================
# QUICK DOWNLOAD
# =====================================================

st.subheader("📥 Export Dashboard")

c1,c2,c3 = st.columns(3)

with c1:

    st.download_button(

        "⬇ Download CSV",

        data="Sample Report",

        file_name="dashboard.csv"

    )

with c2:

    st.download_button(

        "⬇ Download TXT",

        data="Dashboard Report",

        file_name="dashboard.txt"

    )

with c3:

    st.button(

        "📄 Generate PDF",

        use_container_width=True

    )

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<hr>

<div style='text-align:center;'>

<h4>📞 SmartCall AI Dashboard</h4>

<p>
AI Powered Call Center Escalation Risk Prediction
</p>

<p>

Version 1.0 | Team Project | 2026

</p>

</div>

""", unsafe_allow_html=True)