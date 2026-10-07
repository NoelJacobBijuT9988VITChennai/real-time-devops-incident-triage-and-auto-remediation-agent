"""
Hybrid Root Cause Analysis Agent
"""


def perform_rca(
    log_result,
    metric_result,
    event
):

    message = str(
        event.get("message", "")
    ).lower()

    status_code = int(
        event.get("status_code", 200)
    )

    duration_ms = int(
        event.get("duration_ms", 0)
    )

    # Derive level from status code
    if status_code >= 500:
        level = "ERROR"

    elif status_code >= 400:
        level = "WARNING"

    else:
        level = "INFO"

    if (
        "timeout" in message
        or "database" in message
        or "connection refused" in message
    ):

        return {
            "root_cause":
                "Database Connectivity Problem",

            "confidence":
                0.92,

            "explanation":
                "Database timeout or connection failure detected."
        }

    if duration_ms > 10000:

        return {
            "root_cause":
                "Application Performance Degradation",

            "confidence":
                0.88,

            "explanation":
                "Request duration exceeded threshold."
        }

    if status_code >= 500:

        return {
            "root_cause":
                "Backend Service Failure",

            "confidence":
                0.85,

            "explanation":
                "Server returned 5xx error."
        }

    if level in ["ERROR", "CRITICAL"]:

        return {
            "root_cause":
                "Application Runtime Failure",

            "confidence":
                0.80,

            "explanation":
                "Critical application error detected."
        }

    return {
        "root_cause":
            "Unknown",

        "confidence":
            0.50,

        "explanation":
            "Unable to determine root cause."
    }