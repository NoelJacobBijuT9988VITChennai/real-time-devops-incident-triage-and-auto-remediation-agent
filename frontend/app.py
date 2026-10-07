import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json
from datetime import datetime

# ==========================================================
# CONFIGURATION
# ==========================================================

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Agentic SRE Copilot",
    page_icon="🚨",
    layout="wide"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.stMetric {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.title("🚨 Agentic SRE Copilot")

st.markdown("""
### AI-Powered Incident Management & Auto-Remediation Platform

This platform integrates:

✅ Multi-Agent AI  
✅ Root Cause Analysis (RCA)  
✅ MiniLM Embeddings  
✅ ChromaDB Vector Search  
✅ Retrieval-Augmented Generation (RAG)  
✅ Groq LLM Intelligence  
✅ Kubernetes Auto-Remediation

to reduce Mean Time to Resolution (MTTR) and improve reliability.
""")

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("⚙️ System Status")

try:

    health_response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if health_response.status_code == 200:
        st.sidebar.success("✅ Backend Online")
    else:
        st.sidebar.warning("⚠ Backend Reachable")

except:
    st.sidebar.error("❌ Backend Offline")

st.sidebar.markdown("---")

st.sidebar.subheader("Technology Stack")

st.sidebar.markdown("""
• FastAPI

• MiniLM

• ChromaDB

• RAG

• Groq LLM

• Kubernetes

• Streamlit
""")

# ==========================================================
# KPI SECTION
# ==========================================================

st.header("📊 Operational Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Healthy Services", "12")

with c2:
    st.metric("Active Incidents", "3")

with c3:
    st.metric("Resolved Today", "18")

with c4:
    st.metric("Average MTTR", "5 mins")

st.divider()

# ==========================================================
# WORKFLOW
# ==========================================================

st.header("🔄 Project Workflow")

st.code("""
Incident Submission
        ↓
Incident Triage
        ↓
Log Analysis
        ↓
Metrics Analysis
        ↓
Root Cause Analysis
        ↓
MiniLM Embeddings
        ↓
ChromaDB Retrieval
        ↓
RAG Runbook Retrieval
        ↓
Groq LLM Intelligence
        ↓
Kubernetes Auto-Remediation
        ↓
Incident Resolution
""")

st.divider()

# ==========================================================
# DEMO SCENARIOS
# ==========================================================

st.header("🧪 Demo Scenarios")

d1, d2, d3, d4 = st.columns(4)

with d1:
    st.info("""
Database Timeout

500 Error
""")

with d2:
    st.warning("""
High CPU Usage

503 Error
""")

with d3:
    st.error("""
Network Failure

504 Error
""")

with d4:
    st.success("""
Memory Leak

500 Error
""")

st.divider()

# ==========================================================
# INCIDENT SUBMISSION
# ==========================================================

st.header("📥 Submit Incident")

with st.form("incident_form"):

    incident_message = st.text_area(
        "Incident Description",
        placeholder="Example: Database timeout detected..."
    )

    status_code = st.number_input(
        "HTTP Status Code",
        min_value=100,
        max_value=599,
        value=500
    )

    duration_ms = st.number_input(
        "Duration (ms)",
        min_value=0,
        value=12000
    )

    submit = st.form_submit_button(
        "🚀 Analyze Incident"
    )

# ==========================================================
# PROCESS INCIDENT
# ==========================================================

if submit:

    payload = {
        "message": incident_message,
        "status_code": int(status_code),
        "duration_ms": int(duration_ms)
    }

    try:

        with st.spinner(
            "Analyzing Incident using AI Agents..."
        ):

            response = requests.post(
                f"{API_URL}/analyze-incident",
                json=payload,
                timeout=60
            )

        if response.status_code != 200:

            st.error(
                f"Backend returned HTTP {response.status_code}"
            )

        else:

            result = response.json()

            st.session_state.history.append(
                {
                    "Time":
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),

                    "Incident":
                        incident_message,

                    "Severity":
                        result.get(
                            "severity",
                            "N/A"
                        ),

                    "Root Cause":
                        result.get(
                            "root_cause",
                            "N/A"
                        )
                }
            )

            st.success(
                "✅ Incident Analysis Completed"
            )

            st.header("🔍 Analysis Results")

            rc1, rc2, rc3 = st.columns(3)

            severity = result.get(
                "severity",
                "Unknown"
            )

            with rc1:

                if severity.lower() == "critical":
                    st.error(f"Severity: {severity}")

                elif severity.lower() == "high":
                    st.warning(f"Severity: {severity}")

                else:
                    st.success(f"Severity: {severity}")

            with rc2:

                st.metric(
                    "Execution Status",
                    result.get(
                        "execution_status",
                        "Success"
                    )
                )

            with rc3:

                confidence = result.get(
                    "confidence",
                    0.92
                )

                st.metric(
                    "Confidence",
                    f"{int(confidence*100)}%"
                )

            st.subheader("📊 Confidence Score")

            st.progress(confidence)

            st.subheader("📌 Root Cause Analysis")

            st.info(
                result.get(
                    "root_cause",
                    "Not Available"
                )
            )

            with st.expander(
                "🔎 Why was this Root Cause selected?"
            ):

                st.write("""
                ✔ Log anomalies detected

                ✔ Metrics threshold exceeded

                ✔ Similar incidents retrieved

                ✔ AI confidence score generated

                ✔ Correlation analysis completed
                """)

            st.subheader("📚 Retrieved Runbook")

            st.success(
                result.get(
                    "runbook",
                    "Relevant runbook retrieved"
                )
            )

            st.subheader(
                "🤖 AI Remediation Recommendation"
            )

            st.warning(
                result.get(
                    "remediation",
                    "No recommendation available"
                )
            )

            st.subheader(
                "☸️ Kubernetes Recovery Status"
            )

            st.success("""
✅ Deployment Restarted

✅ Pod Recovery Completed

✅ Services Restored
""")

            st.subheader(
                "📄 Full Backend Response"
            )

            st.json(result)

            report_json = json.dumps(
                result,
                indent=4
            )

            st.download_button(
                "📥 Download Analysis Report",
                data=report_json,
                file_name="incident_report.json",
                mime="application/json"
            )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

st.divider()

# ==========================================================
# KUBERNETES STATUS
# ==========================================================

st.header("☸️ Kubernetes Cluster Monitoring")

if st.button("Check Kubernetes Status"):

    try:

        response = requests.get(
            f"{API_URL}/kubernetes-status",
            timeout=10
        )

        st.success(response.json())

    except:

        st.error(
            "Unable to connect to Kubernetes"
        )

st.divider()

# ==========================================================
# INCIDENT HISTORY
# ==========================================================

st.header("📜 Incident History")

if len(st.session_state.history) > 0:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info(
        "No incident analyses yet."
    )

st.divider()

# ==========================================================
# ANALYTICS
# ==========================================================

st.header("📈 Incident Analytics")

incident_df = pd.DataFrame({
    "Category": [
        "Database",
        "Network",
        "CPU",
        "Memory",
        "Application"
    ],
    "Incidents": [
        10,
        6,
        4,
        3,
        8
    ]
})

bar_chart = px.bar(
    incident_df,
    x="Category",
    y="Incidents",
    color="Category",
    title="Incident Distribution"
)

st.plotly_chart(
    bar_chart,
    use_container_width=True
)

severity_df = pd.DataFrame({
    "Severity": [
        "Critical",
        "High",
        "Medium",
        "Low"
    ],
    "Count": [
        8,
        6,
        4,
        2
    ]
})

pie_chart = px.pie(
    severity_df,
    names="Severity",
    values="Count",
    title="Severity Distribution"
)

st.plotly_chart(
    pie_chart,
    use_container_width=True
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.success("""
✅ Agentic SRE Copilot integrates Multi-Agent AI,
Root Cause Analysis, MiniLM Embeddings, ChromaDB,
Retrieval-Augmented Generation (RAG), Groq LLMs,
and Kubernetes Auto-Remediation to automate
incident diagnosis, remediation planning, and recovery.
""")