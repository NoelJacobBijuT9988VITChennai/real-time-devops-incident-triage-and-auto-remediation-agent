# 🚀 Agentic SRE Copilot

## 📌 Overview

Agentic SRE Copilot is an AI-powered incident management and auto-remediation platform designed for cloud-native environments. The system automates incident detection, triage, root cause analysis, runbook retrieval, remediation planning, and Kubernetes-based recovery using Multi-Agent AI, RAG, MiniLM, ChromaDB, Groq LLMs, and Kubernetes.

---

## 🎯 Key Benefits

- ⚡ Reduced Mean Time to Resolution (MTTR)
- 🤖 Automated Incident Analysis
- 🔍 Intelligent Root Cause Analysis (RCA)
- 📚 RAG-Based Runbook Retrieval
- ☸️ Kubernetes Auto-Remediation
- 🛡️ Improved Service Reliability
- 🔄 Self-Healing Infrastructure

---

## 🏗️ Architecture

```text
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
```

---

## 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| 💻 Language | Python |
| 🌐 Backend | FastAPI |
| 📖 API Documentation | Swagger UI |
| 🤖 LLM | Groq |
| 🧠 Embeddings | MiniLM |
| 🔎 Retrieval | RAG |
| 🗄️ Vector Database | ChromaDB |
| ☸️ Container Orchestration | Kubernetes |
| 🔗 Workflow | Multi-Agent Architecture |
| 📂 Version Control | Git & GitHub |

---

## 📦 Project Modules

| Module | Function |
|----------|----------|
| 📥 Incident Ingestion | Collects incident data, logs, and metrics |
| 🚦 Incident Triage | Prioritizes incidents based on severity |
| 📄 Log Analysis | Detects errors and anomalies from logs |
| 📊 Metrics Analysis | Analyzes latency and performance metrics |
| 🔍 Root Cause Analysis | Identifies the underlying cause of incidents |
| 📚 RAG Runbook Retrieval | Retrieves relevant troubleshooting guides |
| 📝 Remediation Planning | Generates recovery recommendations |
| 🤖 LLM Intelligence | Provides reasoning and decision support |
| ☸️ Kubernetes Auto-Remediation | Performs restart, scaling, and recovery |
| 🔄 Workflow Orchestration | Coordinates end-to-end workflow |

---

## 📡 API Endpoints

### 🏠 GET /

Returns a welcome message indicating that the Agentic SRE Copilot service is running.

---

### ❤️ GET /health

Checks the health status of the application.

#### Sample Response

```json
{
  "status": "Healthy"
}
```

---

### ☸️ GET /kubernetes-status

Checks Kubernetes cluster connectivity.

#### Sample Response

```json
{
  "status": "Connected"
}
```

---

### 🚨 POST /analyze-incident

Analyzes incidents and performs automated remediation.

#### Sample Input

```json
{
  "message": "Database timeout detected",
  "status_code": 500,
  "duration_ms": 12000
}
```

#### Sample Output

```json
{
  "severity": "Critical",
  "root_cause": "Database Connectivity Problem",
  "remediation": "Restart Deployment",
  "execution_status": "Success"
}
```
## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<username>/agentic-sre-copilot.git
cd agentic-sre-copilot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

#### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Execution Flow

### 🧠 Test Embedding Model

```bash
python test_embedding.py
```

### 📚 Load Runbooks into ChromaDB

```bash
python rag/load_runbooks.py
```

### 🔎 Test RAG Retrieval

```bash
python test_rag.py
```

### ☸️ Test Kubernetes Connectivity

```bash
python test_kubernetes.py
```

### 🚀 Test Complete Workflow

```bash
python test_workflow.py
```

### 🌐 Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## 📖 Swagger UI

Access the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Objectives

- ✅ Automate incident management and analysis
- ✅ Reduce Mean Time to Resolution (MTTR)
- ✅ Improve root cause identification accuracy
- ✅ Enable intelligent runbook retrieval using RAG
- ✅ Perform Kubernetes-based remediation
- ✅ Build self-healing cloud-native infrastructure

---

## 📈 Expected Outcomes

- ⚡ Faster incident resolution
- 🤖 Reduced manual intervention
- 🛡️ Improved service reliability
- 📚 Intelligent troubleshooting assistance
- ☸️ Automated Kubernetes recovery
- 🔄 Self-healing infrastructure

---

## 🔮 Future Enhancements

- 📈 Predictive Incident Detection
- 🤖 Advanced Anomaly Detection
- ☸️ Multi-Cluster Kubernetes Support
- 📊 Prometheus & Grafana Integration
- 🔄 Automated Approval Workflows
