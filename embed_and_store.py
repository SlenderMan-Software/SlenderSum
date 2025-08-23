# Import the pysqlite3 module and alias it as sqlite3 for compatibility
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables from a .env file
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # For embedding generation
from langchain_chroma import Chroma  # For vector store management

# Load environment variables from a .env file
load_dotenv()

# Initialize the embedding model using Google Generative AI
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Initialize the Chroma vector store with a specific collection name and persistence directory
vector_store = Chroma(
    collection_name="knotebooklm",  # Name of the collection in the vector store
    embedding_function=embeddings,  # Embedding function to generate vector representations
    persist_directory="./chroma_langchain_db",  # Directory to persist the vector store
)

# Function to add documents to the vector store
def add_documents(documents):
    """
    Add a list of documents to the vector store.

    Args:
        documents (list): A list of documents to be added.

    Returns:
        The result of adding the documents to the vector store.
    """
    return vector_store.add_documents(documents=documents)
