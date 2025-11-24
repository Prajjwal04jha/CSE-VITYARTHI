# 📚 Mini Vector Database (with Gradio UI + MiniLM Embeddings)

A beginner-friendly project to learn *vector databases, **embeddings, **semantic search, and **Gradio app development* — all using pure Python.

This project is perfect for first-semester students who want to understand how modern AI search systems work under the hood.

---

## ✨ What This Project Does

This project lets you:

### ✅ Create collections  
Think of these like folders to organize your data.

### ✅ Add text to a collection  
Each text is automatically converted into a *vector* using the MiniLM sentence-transformer model.

### ✅ Store vectors + metadata in a JSON file  
No SQL, no FAISS, no external DB — just pure Python + NumPy.

### ✅ Update or delete stored items  
Fully supports CRUD operations.

### ✅ Search using semantic similarity  
Ask a question → find similar stored text (via cosine similarity).

### ✅ Use a clean Gradio Web App  
Everything runs in your browser. Zero HTML needed.

---

## 🧠 What is a Vector Database?

A vector database stores information as *vectors* (lists of numbers).  
These vectors represent meaning.

For example:

- “The capital of France is Paris.”  
- “Eiffel Tower is in Paris.”

These sentences will produce similar vector values.

Using these vectors, we can perform *semantic search*, which is more powerful than keyword search.

---

## 🏗 Project Structure
