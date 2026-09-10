from sentence_transformers import SentenceTransformer

MODEL_PATH = "models/all-MiniLM-L6-v2"

model = SentenceTransformer(
    MODEL_PATH,
    local_files_only=True
)

embedding = model.encode(
    "Database connectivity problem"
)

print(
    f"Embedding Dimension: {len(embedding)}"
)