from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

MODEL_PATH = "models/all-MiniLM-L6-v2"

VECTOR_DB_PATH = "vector_db"

embedding_model = HuggingFaceEmbeddings(
    model_name=MODEL_PATH,
    model_kwargs={
        "local_files_only": True
    }
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