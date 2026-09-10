from rag.retrieval import (
    retrieve_runbook
)
query = (
    "Database Connectivity Problem"
)
result = retrieve_runbook(
    "Database Connectivity Problem"
)
print(result)