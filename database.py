import os
import json
import uuid
import numpy as np


class VectorDB:
    """
    A simple JSON-backed vector database that stores
    collections of (vector + metadata) records on disk.
    """

    def __init__(self, path="vector_db.json"):
        self.path = path
        self.collections = {}

        # Load DB if it exists, otherwise create empty file
        if os.path.exists(self.path):
            self._load()
        else:
            self._save()

    def _save(self):
        """Write the in-memory collections to disk in JSON format."""

        serializable = {}
        for cname, items in self.collections.items():
            serializable[cname] = {}
            for record_id, record in items.items():
                serializable[cname][record_id] = {
                    "vector": record["vector"].tolist(),
                    "metadata": record["metadata"]
                }

        with open(self.path, "w") as f:
            json.dump(serializable, f, indent=2)

    def _load(self):
        """Load collections from the JSON file into memory."""

        with open(self.path, "r") as f:
            data = json.load(f)

        for cname, items in data.items():
            self.collections[cname] = {}
            for record_id, record in items.items():
                self.collections[cname][record_id] = {
                    "vector": np.array(record["vector"], dtype=float),
                    "metadata": record["metadata"]
                }


    def create_collection(self, name):
        """Create a new empty collection."""

        if name in self.collections:
            return f"Collection '{name}' already exists."

        self.collections[name] = {}
        self._save()
        return f"Created collection: {name}"

    def list_collections(self):
        """Return a list of existing collection names."""
        return list(self.collections.keys())


    def add(self, collection, vector, metadata):
        """Insert a new vector + metadata record into a collection."""

        if collection not in self.collections:
            return "Collection not found!"

        record_id = str(uuid.uuid4())

        if not isinstance(vector, np.ndarray):
            vector = np.array(vector, dtype=float)

        self.collections[collection][record_id] = {
            "vector": vector,
            "metadata": metadata
        }

        self._save()
        return record_id

    def update(self, collection, record_id, new_metadata):
        """Update metadata of an existing record."""

        if collection not in self.collections:
            return "Collection not found!"
        if record_id not in self.collections[collection]:
            return "ID does not exist!"

        self.collections[collection][record_id]["metadata"] = new_metadata
        self._save()
        return f"Updated metadata for {record_id}"

    def delete(self, collection, record_id):
        """Delete a record from a collection."""

        if collection not in self.collections:
            return "Collection not found!"
        if record_id not in self.collections[collection]:
            return "ID not found!"

        del self.collections[collection][record_id]
        self._save()
        return f"Deleted {record_id}"

    def search(self, collection, query_vector, top_k=3):
        """Return top_k vectors sorted by cosine similarity."""

        if collection not in self.collections:
            return []

        if not isinstance(query_vector, np.ndarray):
            query_vector = np.array(query_vector, dtype=float)

        results = []
        for record_id, rec in self.collections[collection].items():
            sim = self.cosine_similarity(query_vector, rec["vector"])
            results.append((record_id, sim, rec["metadata"]))

        # Sort by highest similarity
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]

    @staticmethod
    def cosine_similarity(a, b):
        """Compute cosine similarity between two vectors."""
        dot = np.dot(a, b)
        denom = np.linalg.norm(a) * np.linalg.norm(b)
        return float(dot / denom) if denom > 0 else 0.0
