from rag.retrieval import (
    retrieve_runbook
)

result = retrieve_runbook(
    "Database Connectivity Problem"
)

print(result)