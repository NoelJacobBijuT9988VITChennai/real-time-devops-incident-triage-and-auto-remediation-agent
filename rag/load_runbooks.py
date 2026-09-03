"""
Load runbooks into ChromaDB.
"""

import os

from langchain.schema import Document

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    SentenceTransformerEmbeddings
)

from config import (
    EMBEDDING_MODEL_PATH,
    VECTOR_DB_PATH
)

documents = []

runbook_folder = "datasets/runbooks"

for file in os.listdir(runbook_folder):

    if file.endswith(".md"):

        path = os.path.join(
            runbook_folder,
            file
        )

        with open(
            path,
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

embedding_model = (
    SentenceTransformerEmbeddings(
        model_name=EMBEDDING_MODEL_PATH
    )
)

db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=VECTOR_DB_PATH
)

db.persist()

print(
    "Vector database created successfully."
)