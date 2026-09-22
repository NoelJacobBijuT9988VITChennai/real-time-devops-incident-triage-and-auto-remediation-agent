🚀 Agentic SRE Copilot
📌 Overview

Agentic SRE Copilot is an AI-powered incident management and auto-remediation platform designed for cloud-native environments. The system automates incident detection, triage, root cause analysis, runbook retrieval, remediation planning, and Kubernetes-based recovery using Multi-Agent AI, RAG, MiniLM, ChromaDB, Groq LLMs, and Kubernetes.

🎯 Key Benefits
⚡ Reduced Mean Time to Resolution (MTTR)
🤖 Automated Incident Analysis
🔍 Intelligent Root Cause Analysis (RCA)
📚 RAG-Based Runbook Retrieval
☸️ Kubernetes Auto-Remediation
🛡️ Improved Service Reliability
🔄 Self-Healing Infrastructure

🏗️ Architecture
Incident Submission
        ↓
📥 Incident Ingestion
        ↓
🚦 Incident Triage
        ↓
📄 Log Analysis
        ↓
📊 Metrics Analysis
        ↓
🔍 Root Cause Analysis
        ↓
🧠 MiniLM Embeddings
        ↓
🗄️ ChromaDB Vector Search
        ↓
📚 RAG Runbook Retrieval
        ↓
📝 Remediation Planning
        ↓
🤖 LLM Intelligence
        ↓
☸️ Kubernetes Auto-Remediation
        ↓
✅ Incident Resolution

🛠️ Technology Stack
| Category                   | Technology               |
| -------------------------- | ------------------------ |
| 💻 Language                | Python                   |
| 🌐 Backend                 | FastAPI                  |
| 📖 API Documentation       | Swagger UI               |
| 🤖 LLM                     | Groq                     |
| 🧠 Embeddings              | MiniLM                   |
| 🔎 Retrieval               | RAG                      |
| 🗄️ Vector Database        | ChromaDB                 |
| ☸️ Container Orchestration | Kubernetes               |
| 🔗 Workflow                | Multi-Agent Architecture |
| 📂 Version Control         | Git & GitHub             |

📦 Project Modules
| Module                         | Function                                     |
| ------------------------------ | -------------------------------------------- |
| 📥 Incident Ingestion          | Collects incident data, logs, and metrics    |
| 🚦 Incident Triage             | Prioritizes incidents based on severity      |
| 📄 Log Analysis                | Detects errors and anomalies from logs       |
| 📊 Metrics Analysis            | Analyzes latency and performance metrics     |
| 🔍 Root Cause Analysis         | Identifies the underlying cause of incidents |
| 📚 RAG Runbook Retrieval       | Retrieves relevant troubleshooting guides    |
| 📝 Remediation Planning        | Generates recovery recommendations           |
| 🤖 LLM Intelligence            | Provides reasoning and decision support      |
| ☸️ Kubernetes Auto-Remediation | Performs restart, scaling, and recovery      |
| 🔄 Workflow Orchestration      | Coordinates end-to-end workflow              |

📡 API Endpoints
🏠 GET /
Returns a welcome message.

❤️ GET /health
Checks application health.
{
  "status": "Healthy"
}

☸️ GET /kubernetes-status
Checks Kubernetes connectivity.

🚨 POST /analyze-incident
Analyzes incidents and performs remediation.
Sample Input
{
  "message": "Database timeout detected",
  "status_code": 500,
  "duration_ms": 12000
}
Sample Output
{
  "severity": "Critical",
  "root_cause": "Database Connectivity Problem",
  "remediation": "Restart Deployment",
  "execution_status": "Success"
}

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/<username>/agentic-sre-copilot.git
cd agentic-sre-copilot
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Virtual Environment
Windows
.\venv\Scripts\Activate.ps1
Linux/macOS
source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Execution Flow
🧠 Test Embedding Model
python test_embedding.py
📚 Load Runbooks into ChromaDB
python rag/load_runbooks.py
🔎 Test RAG Retrieval
python test_rag.py
☸️ Test Kubernetes Connection
python test_kubernetes.py
🚀 Run Complete Workflow
python test_workflow.py
🌐 Start FastAPI Server
uvicorn app.main:app --reload
📖 Swagger UI
Access interactive API documentation:
http://127.0.0.1:8000/docs

🎯 Objectives
✅ Automate incident management
✅ Reduce MTTR
✅ Improve root cause identification
✅ Enable intelligent runbook retrieval
✅ Perform Kubernetes-based remediation
✅ Build self-healing cloud-native systems

📈 Expected Outcomes
⚡ Faster incident resolution
🤖 Reduced manual intervention
🛡️ Improved system reliability
📚 Intelligent troubleshooting assistance
☸️ Automated Kubernetes recovery
🔄 Self-healing infrastructure

🔮 Future Enhancements
📈 Predictive Incident Detection
🤖 Advanced Anomaly Detection
☸️ Multi-Cluster Kubernetes Support
📊 Prometheus & Grafana Integration
🔄 Automated Approval Workflows
