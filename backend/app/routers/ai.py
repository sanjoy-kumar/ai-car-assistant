from fastapi import APIRouter
from openai import OpenAI
import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from ..cache import redis_client
from ..utils import generate_cache_key

load_dotenv()

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Vector database
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("car_knowledge")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


@router.post("/ask")
def ask_ai(data: dict):

    cache_key = generate_cache_key(data)
    cached = redis_client.get(cache_key)

    if cached:
        return {
            "answer": cached,
            "cached": True
        }

    question = data["question"]
    query_embedding = embedding_model.encode([question])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    context = results["documents"][0]

    prompt = f"""
        You are a professional car mechanic.

        Knowledge Base:
        {context}

        Car Information
        Make: {data['make']} 
        Model: {data['model']}
        Year: {data['year']}
        Mileage: {data['mileage']}

        Question:
        {question}

        Provide:
        1. Possible causes
        2. Estimated repair cost
        3. Recommendation
        """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    redis_client.set(cache_key, answer, ex=3600)

    return {
        "answer": answer,
        "cached": False
    }
