import chromadb
from sentence_transformers import SentenceTransformer
import os
import logging
from transformers import logging as transformers_logging

# This will hide the "Unexpected Key" warnings
transformers_logging.set_verbosity_error()

# 1. Initialize Persistent Client (saves to a 'chroma_db' folder)
# This ensures your data stays on the disk
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Create or Get Collection
collection = client.get_or_create_collection("car_knowledge")

# 3. Load Model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Brake squeaking usually indicates worn brake pads.",
    "Oil should be changed every 5000 miles.",
    "Engine overheating may indicate coolant leak.",
    "Tire rotation should happen every 6000 miles.",
    "Battery failure may occur if voltage drops below normal levels."
]

# 4. Generate Embeddings and IDs
# Chroma expects lists, not numpy arrays
embeddings = model.encode(documents).tolist()
ids = [str(i) for i in range(len(documents))]

# 5. Batch Add (Much faster than a loop)
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print(f"Knowledge base created and saved to {os.getcwd()}/chroma_db")
