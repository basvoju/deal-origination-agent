from openai import OpenAI
from config import EMBEDDING_MODEL

client = OpenAI()

def create_embedding(text):

    response = client.embeddings.create(
        input=text,
        model=EMBEDDING_MODEL
    )

    return response.data[0].embedding