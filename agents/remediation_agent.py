"""
Remediation Agent

Generate recovery actions
based on RCA results.
"""


def create_plan(
    root_cause,
    runbook
):

    if "Database" in root_cause:

        return {
            "action": "restart_deployment",
            "target": "database-service"
        }

    elif "Latency" in root_cause:

        return {
            "action": "scale_deployment",
            "target": "payment-service",
            "replicas": 5
        }

    else:

        return {
            "action": "manual_review"
        }