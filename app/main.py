from fastapi import FastAPI

from kubernetes import config

from workflows.incident_graph import run_workflow

from schemas.incident import IncidentRequest

app = FastAPI(
    title="Agentic SRE Copilot",
    description="AI-Powered Incident Management and Auto-Remediation Platform",
    version="1.0.0"
)


def get_kubernetes_status():

    try:

        config.load_kube_config()

        return "Connected"

    except Exception:

        return "Simulation Mode"


@app.get("/")
def home():

    return {
        "project": "Agentic SRE Copilot",
        "swagger_ui": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():

    return {
        "status": "Healthy"
    }


@app.get("/kubernetes-status")
def kubernetes_status():

    return {
        "status": get_kubernetes_status()
    }


@app.post("/analyze-incident")
def analyze_incident(
    event: IncidentRequest
):

    return run_workflow(
        event.model_dump()
    )