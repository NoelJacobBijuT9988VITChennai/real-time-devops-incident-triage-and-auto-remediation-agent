from agents.triage_agent import triage
from agents.log_agent import analyze_logs
from agents.metrics_agent import analyze_metrics
from agents.rca_agent import perform_rca

from agents.remediation_agent import create_plan

from agents.executor_agent import (
    restart_deployment,
    scale_deployment
)

from rag.retrieval import retrieve_runbook


def run_workflow(event):

    triage_result = triage(event)

    log_result = analyze_logs(event)

    metric_result = analyze_metrics(event)

    rca_result = perform_rca(
        log_result,
        metric_result,
        event
    )

    runbook = retrieve_runbook(
        rca_result["root_cause"]
    )

    remediation = create_plan(
        rca_result["root_cause"],
        runbook
    )

    execution_result = {
        "status": "Not Executed"
    }

    try:

        if remediation["action"] == "restart_deployment":

            execution_result = restart_deployment(
                remediation["target"]
            )

        elif remediation["action"] == "scale_deployment":

            execution_result = scale_deployment(
                remediation["target"],
                remediation["replicas"]
            )

    except Exception as e:

        execution_result = {
            "status": "Failed",
            "message": str(e)
        }

    return {
        "triage": triage_result,
        "log_analysis": log_result,
        "metrics_analysis": metric_result,
        "root_cause": rca_result,
        "runbook": runbook,
        "remediation": remediation,
        "execution": execution_result
    }