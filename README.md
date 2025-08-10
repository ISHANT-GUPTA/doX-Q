# 🧠 doXQ – Metadata-Aware RAG System for Document Understanding

**doX-Q** is an AI-powered document understanding system designed to process unstructured text in PDFs and other formats using **Large Language Models (LLMs)**. It enables users to upload documents, ask natural language questions, and receive structured, explainable responses based on the content of those documents.  
It leverages **Retrieval-Augmented Generation (RAG)** with metadata-aware embeddings to find relevant clauses and generate answers with justifications — making it suitable for sensitive, rule-based domains like **insurance**, **legal compliance**, and **contract management**.

---

## 🚀 Features

- **📂 Multi-format Document Ingestion**  
  Supports PDFs, DOCX, TXT, HTML, and email formats.

- **🔍 Metadata Extraction Pipeline**  
  Automatically extracts **titles, sample QAs**, and other contextual metadata.

- **💡 Metadata-Enhanced Embeddings**  
  Metadata is embedded alongside the main document content to improve semantic search accuracy.

- **🔐 Secure, Privacy-Preserving Vector Store**  
  Embeddings are stored in **local, self-hosted vector databases** (e.g., ChromaDB) to ensure complete control over sensitive data, making doXQ suitable for compliance-heavy environments.

- **🧾 Clause-Level Citation**  
  Every answer is linked back to the **exact source fragment** for transparency and auditability.

---


## 🏗 Architecture Overview

       ┌────────────────────────────┐
       │       Document Parser      │
       └─────────────┬──────────────┘
                     ▼
       ┌────────────────────────────┐
       │  Metadata Extraction Layer │
       │    (Title, Few shot QA)    │
       └─────────────┬──────────────┘
                     ▼
       ┌────────────────────────────┐
       │   Text & Metadata Embedder │
       └─────────────┬──────────────┘
                     ▼
       ┌────────────────────────────┐
       │     Create vector index    │
       └─────────────┬──────────────┘
                     ▼
       ┌────────────────────────────┐
       │    Retrieval + Reranking   │
       └─────────────┬──────────────┘
                     ▼
       ┌────────────────────────────┐
       │     LLM response synthesis │
       └────────────────────────────┘



---

## ⚙️ Installation

**Prerequisites**  
- Python **3.11+**  
- [`uv`](https://github.com/astral-sh/uv) – Python package manager

```bash
git clone https://github.com/ISHANT-GUPTA/doX-Q.git

cd doX-Q

uv sync --locked
```

---
## 🚀 Roadmap

Planned enhancements to make **doX-Q** even more powerful and production-ready:

- **📊 Configurable Retrieval Strategies**  
  Hybrid search (**dense embeddings + BM25**) and metadata-filtered retrieval.

- **🛠 Modular Architecture**  
  Easily swap components like embedding models, databases, or LLM backends.

- **🧠 Adaptive Reranking**  
  Introduce machine-learning–driven reranking strategies that adapt based on user feedback.

- **🔗 Knowledge Graph Integration**  
  Enrich embeddings and retrieval with semantic relationships between entities for deeper reasoning capabilities.

