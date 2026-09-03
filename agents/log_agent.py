"""
Analyze application logs.
"""

def analyze_logs(event):

    message = str(
        event["message"]
    ).lower()

    level = str(
        event["level"]
    ).upper()

    if "timeout" in message:

        return {
            "issue": "Database Timeout",
            "confidence": 0.92
        }

    if "connection refused" in message:

        return {
            "issue": "Database Connection Failure",
            "confidence": 0.90
        }

    if level in ["ERROR", "CRITICAL"]:

        return {
            "issue": "Application Failure",
            "confidence": 0.85
        }

    return {
        "issue": "Unknown",
        "confidence": 0.50
    }