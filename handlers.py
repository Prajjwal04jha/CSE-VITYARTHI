from sentence_transformers import SentenceTransformer
from vectordb.database import VectorDB

db = VectorDB()
model = SentenceTransformer("all-MiniLM-L6-v2")


def ui_create_collection(name):
    msg = db.create_collection(name)
    return msg, db.list_collections()


def ui_add_text(collection, text):
    embedding = model.encode(text)
    record_id = db.add(collection, embedding, {"text": text})
    return f"Inserted ID: {record_id}"


def ui_update_metadata(collection, record_id, metadata_text):
    return db.update(collection, record_id, {"text": metadata_text})


def ui_delete(collection, record_id):
    return db.delete(collection, record_id)


def ui_search(collection, query, top_k):
    embedding = model.encode(query)
    results = db.search(collection, embedding, top_k)

    if not results:
        return "No results."

    out = []
    for record_id, score, metadata in results:
        out.append(
            f"ID: {record_id}\nSimilarity: {score:.4f}\nText: {metadata['text']}\n"
        )

    return "\n".join(out)
