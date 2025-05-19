import chromadb

client = chromadb.PersistentClient(path="/workspaces/KnotebookLM_summary_engine/chroma_langchain_db")
collection = client.get_collection('knotebooklm')

def list_docs(doc_id):
    result = collection.get(where={ "document_id": doc_id }, include=[])
    return result["ids"]

def delete_docs(doc_id):
    collection.delete(where={ "document_id": doc_id })
    return True