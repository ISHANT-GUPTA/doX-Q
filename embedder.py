from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

current_dir = os.getcwd()
persistent_dir = os.path.join(current_dir, "db", "doc_embeddings")

file_path = "doc.pdf"

loader = PyPDFLoader(file_path=file_path)
documents = loader.load()
print(len(documents))

splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=200)
docs = splitter.split_documents(documents=documents)

print(f"Number of document chunks: {len(docs)}")

print("\nCreating Embeddings")
embeddings = OllamaEmbeddings(
    model="bge-m3"
)
print("==========Finished creating embeddings===============")

print("\n\nCreating vector store")
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory=persistent_dir
)
print("Finished creating vector store")