from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import VECTOR_DB_PATH

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="./models/all-MiniLM-L6-v2"
)

# Load Chroma DB
db = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embedding_model
)

print(
    "Documents in Vector DB:",
    db._collection.count()
)


def retrieve_runbook(query: str):

    # Handle empty queries
    if not query:
        query = "Unknown Incident"

    query = str(query).strip()

    if len(query) == 0:
        query = "Unknown Incident"

    print("Query:", query)

    results = db.similarity_search(
        query,
        k=3
    )

    print("Results:", results)

    if not results:
        return "No runbook found."

    return results[0].page_content