"""
Semantic runbook retrieval.
"""

from langchain_community.vectorstores import (
    Chroma
)

from langchain_community.embeddings import (
    SentenceTransformerEmbeddings
)

from config import (
    EMBEDDING_MODEL_PATH,
    VECTOR_DB_PATH
)

embedding_model = (
    SentenceTransformerEmbeddings(
        model_name=EMBEDDING_MODEL_PATH
    )
)

db = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embedding_model
)


def retrieve_runbook(query):

    docs = db.similarity_search(
        query,
        k=1
    )

    if docs:
        return docs[0].page_content

    return "No runbook found."