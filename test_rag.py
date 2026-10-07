from rag.retrieval import retrieve_runbook

query = "Database timeout detected"

print("\nTesting Query:")
print(query)

result = retrieve_runbook(query)

print("\nRetrieved Runbook:")
print(result)