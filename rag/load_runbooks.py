import os

from langchain.schema import Document

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

MODEL_PATH = "models/all-MiniLM-L6-v2"

VECTOR_DB_PATH = "vector_db"

RUNBOOK_FOLDER = "datasets/runbooks"

documents = []

for file in os.listdir(RUNBOOK_FOLDER):

    if file.endswith(".md"):

        with open(
            os.path.join(
                RUNBOOK_FOLDER,
                file
            ),
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": file
                }
            )
        )

embedding_model = HuggingFaceEmbeddings(
    model_name=MODEL_PATH,
    model_kwargs={
        "local_files_only": True
    }
)

db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=VECTOR_DB_PATH
)

db.persist()

print(
    "Runbooks loaded successfully."
)