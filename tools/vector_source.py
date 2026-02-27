import numpy as np

VECTOR_DB = []

def store_embedding(company, embedding):

    VECTOR_DB.append({
        "company": company,
        "embedding": embedding
    })


def search_similar(query_embedding):

    similarities = []

    for item in VECTOR_DB:

        similarity = np.dot(
            query_embedding,
            item["embedding"]
        )

        similarities.append(
            (similarity, item["company"])
        )

    similarities.sort(reverse=True)

    return similarities[:5]