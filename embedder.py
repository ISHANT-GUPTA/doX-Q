from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import MarkdownTextSplitter, RecursiveCharacterTextSplitter
from llama_cloud_services import LlamaParse
from langchain.schema import Document
import os
from dotenv import load_dotenv

# Load Environment variables
load_dotenv()

# Define the parser
parser = LlamaParse() # type: ignore

# Set vector database directory
current_dir = os.getcwd()
persistent_dir = os.path.join(current_dir, "db", "doc_embeddings")


# Parse the pdf file
file_path = "./test_docs/1_rag_doc.pdf"  # Sample file
result = parser.parse(file_path=file_path)

documents = []
f = open('parsed_md.txt', 'w')
for page in result.pages: # type: ignore
    if not page.md is None:
        documents.append(Document(page_content=page.md)) # type: ignore
        f.write(page.md + "\n\n")
f.close()


# splitter = MarkdownTextSplitter(chunk_size = 2000, chunk_overlap=300)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
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