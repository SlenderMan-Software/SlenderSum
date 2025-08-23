import chromadb

# Initialize a persistent ChromaDB client with the specified database path
client = chromadb.PersistentClient(path="/workspaces/KnotebookLM_summary_engine/chroma_langchain_db")

# Retrieve the collection named 'knotebooklm' from the database
collection = client.get_collection('knotebooklm')

def list_docs(doc_id):
    """
    List document IDs that match the given document_id in the collection.

    Args:
        doc_id (str): The ID of the document to search for.

    Returns:
        list: A list of document IDs that match the query.
    """
    result = collection.get(where={ "document_id": doc_id }, include=[])
    return result["ids"]

def delete_docs(doc_id):
    """
    Delete documents that match the given document_id from the collection.

    Args:
        doc_id (str): The ID of the document to delete.

    Returns:
        bool: True if the operation is successful.
    """
    collection.delete(where={ "document_id": doc_id })
    return True