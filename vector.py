from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Configuration
CSV_FILE = "realistic_restaurant_reviews.csv"
DB_LOCATION = "./chrome_langchain_db"
EMBEDDING_MODEL = "mxbai-embed-large"
COLLECTION_NAME = "restaurant_reviews"
NUM_RESULTS = 5

# Load the reviews CSV
try:
    df = pd.read_csv(CSV_FILE)
    print(f"✅ Loaded {len(df)} reviews from {CSV_FILE}")
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find {CSV_FILE}. Please ensure the file exists.")

# Initialize embeddings
try:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    print(f"✅ Initialized embeddings with model: {EMBEDDING_MODEL}")
except Exception as e:
    raise RuntimeError(f"Failed to initialize embeddings: {e}. Make sure Ollama is running and {EMBEDDING_MODEL} is installed.")

# Check if database already exists
add_documents = not os.path.exists(DB_LOCATION)

# Prepare documents if database doesn't exist
if add_documents:
    print("📚 Creating vector database from reviews...")
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        # Combine title and review for better context
        page_content = f"{row['Title']}. {row['Review']}"
        
        document = Document(
            page_content=page_content,
            metadata={
                "rating": int(row["Rating"]) if pd.notna(row["Rating"]) else None,
                "date": str(row["Date"]) if pd.notna(row["Date"]) else None,
                "title": str(row["Title"]) if pd.notna(row["Title"]) else None
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
    
    print(f"✅ Prepared {len(documents)} documents for indexing")
else:
    print(f"✅ Using existing vector database at {DB_LOCATION}")

# Initialize Chroma vector store
try:
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_LOCATION,
        embedding_function=embeddings
    )
    print(f"✅ Connected to vector database")
except Exception as e:
    raise RuntimeError(f"Failed to initialize vector store: {e}")

# Add documents to database if it's new
if add_documents:
    print("🔄 Indexing documents (this may take a moment)...")
    try:
        vector_store.add_documents(documents=documents, ids=ids)
        print("✅ Successfully indexed all reviews!")
    except Exception as e:
        print(f"⚠️  Warning: Error adding documents: {e}")

# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": NUM_RESULTS}
)

print(f"✅ Retriever ready (will return top {NUM_RESULTS} results)\n")