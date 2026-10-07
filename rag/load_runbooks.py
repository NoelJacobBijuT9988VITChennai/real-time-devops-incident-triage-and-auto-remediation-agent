import os

from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import VECTOR_DB_PATH

RUNBOOKS_DIR = "datasets/runbooks"

documents = []

for filename in os.listdir(RUNBOOKS_DIR):

    if filename.endswith(".md"):

        filepath = os.path.join(
            RUNBOOKS_DIR,
            filename
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": filename
                }
            )
        )

print(
    f"Runbooks Loaded: {len(documents)}"
)

embedding_model = HuggingFaceEmbeddings(
    model_name="./models/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory=VECTOR_DB_PATH
)

print("Vector Database Created Successfully")