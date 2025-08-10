import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, QueryBundle
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

embeddings_model = OllamaEmbedding(
    model_name="bge-m3"
)

load_dotenv()


# initialize client
db = chromadb.PersistentClient(path="./chroma_db")

# get collection
chroma_collection = db.get_or_create_collection("rag_embeddings")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# load your index from stored vectors
index = VectorStoreIndex.from_vector_store(
    vector_store, storage_context=storage_context, embed_model=embeddings_model
)


llm_querying = OpenAI(
    model="gpt-4o-mini",
)
query_engine = index.as_query_engine(llm=llm_querying, embed_model = embeddings_model)
inp = input("You: ")
query = QueryBundle(inp)
response = query_engine.query(inp)
print(response)