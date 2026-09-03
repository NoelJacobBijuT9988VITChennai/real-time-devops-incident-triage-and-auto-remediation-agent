from workflows.incident_graph import run_workflow

event = {

    "message":
    "Database timeout occurred while connecting to PostgreSQL",

    "level":
    "ERROR",

    "status_code":
    500,

    "duration_ms":
    12000,

    "hostname":
    "payment-service-01",

    "trace_id":
    "trace-123"
}

result = run_workflow(event)

print(result)