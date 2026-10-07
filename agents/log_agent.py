"""
Analyze application logs.
"""


def analyze_logs(event):
    """
    Analyze incident logs and identify likely issues.
    """

    message = str(
        event.get("message", "")
    ).lower()

    status_code = int(
        event.get("status_code", 200)
    )

    # Derive log level from status code
    if status_code >= 500:
        level = "ERROR"

    elif status_code >= 400:
        level = "WARNING"

    else:
        level = "INFO"

    if "timeout" in message:

        return {
            "issue": "Database Timeout",
            "confidence": 0.92,
            "level": level
        }

    if "connection refused" in message:

        return {
            "issue": "Database Connection Failure",
            "confidence": 0.90,
            "level": level
        }

    if "cpu" in message:

        return {
            "issue": "High CPU Utilization",
            "confidence": 0.88,
            "level": level
        }

    if "memory" in message:

        return {
            "issue": "Memory Exhaustion",
            "confidence": 0.87,
            "level": level
        }

    if "network" in message:

        return {
            "issue": "Network Connectivity Failure",
            "confidence": 0.89,
            "level": level
        }

    if level in ["ERROR", "CRITICAL"]:

        return {
            "issue": "Application Failure",
            "confidence": 0.85,
            "level": level
        }

    return {
        "issue": "Unknown",
        "confidence": 0.50,
        "level": level
    }