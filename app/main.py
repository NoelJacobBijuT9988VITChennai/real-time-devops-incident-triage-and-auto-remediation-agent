"""
Main FastAPI application.
"""

from fastapi import FastAPI

from workflows.incident_graph import (
    run_workflow
)

app = FastAPI(
    title="Agentic SRE Copilot"
)


@app.get("/")
async def home():

    return {
        "message":
        "Agentic SRE Copilot is running"
    }


@app.post("/incident")
async def process_incident(event: dict):

    result = run_workflow(event)

    return result