from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Function to split a given text into smaller chunks with metadata
def split_text(text, user_id, document_id, notebook_id):
    # Create a Document object with the provided text and metadata
    doc = Document(
        page_content=text, 
        metadata={ 
            "user_id": user_id, 
            "doc_id": document_id, 
            "notebook_id": notebook_id 
        }
    )
    
    # Initialize a RecursiveCharacterTextSplitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=200, 
        add_start_index=True
    )
    
    # Split the document into smaller chunks
    splits = text_splitter.split_documents([doc])
    
    # Return the list of split chunks
    return splits