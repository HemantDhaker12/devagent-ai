import chromadb
from sentence_transformers import SentenceTransformer

# local persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="github_issues"
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def store_issue_memory(issue_id: str, content: str):

    embedding = embedding_model.encode(content).tolist()

    collection.add(
        ids=[issue_id],
        embeddings=[embedding],
        documents=[content]
    )

def retrieve_similar_issues(query: str, n_results: int = 3):

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results