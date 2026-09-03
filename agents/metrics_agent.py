"""
Analyze performance metrics.
"""

def analyze_metrics(event):

    duration = event["duration_ms"]

    status_code = event["status_code"]

    if duration > 5000:

        return {
            "issue": "High Latency"
        }

    if status_code >= 500:

        return {
            "issue": "Server Error"
        }

    return {
        "issue": "Normal"
    }