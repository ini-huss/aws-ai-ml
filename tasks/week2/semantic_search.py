from pathlib import Path

import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer

# Locate the dataset
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "faqs.csv"

# Load and clean the FAQ dataset
df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=["question", "answer"])

df["question"] = df["question"].astype(str).str.strip()
df["answer"] = df["answer"].astype(str).str.strip()

df = df[
    (df["question"] != "")
    & (df["answer"] != "")
].reset_index(drop=True)

# Combine questions and answers
df["text"] = (
    "Question: " + df["question"]
    + "\nAnswer: " + df["answer"]
)

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a persistent Chroma database
client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_or_create_collection(
    name="faq_collection",
    metadata={"hnsw:space": "cosine"}
)

# Split the text into manageable chunks
chunk_size = 3
documents = []

for start in range(0, len(df), chunk_size):
    chunk = df.iloc[start:start + chunk_size]
    documents.extend(chunk["text"].tolist())

# Embed and store the FAQ chunks
embeddings = model.encode(
    documents,
    normalize_embeddings=True
).tolist()

collection.upsert(
    ids=[f"faq_{i}" for i in range(len(documents))],
    documents=documents,
    embeddings=embeddings
)

print(f"Loaded {len(documents)} FAQ documents.")

# Search for the top 3 matches
while True:
    query = input("\nEnter your question (or 'exit'): ").strip()

    if query.lower() == "exit":
        print("Goodbye!")
        break

    if not query:
        print("Please enter a question.")
        continue

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(3, len(documents))
    )

    print("\nTop 3 matches:")

    for rank, document in enumerate(
        results["documents"][0], start=1
    ):
        distance = results["distances"][0][rank - 1]

        print(f"\n{rank}. {document}")
        print(f"Cosine distance: {distance:.4f}")