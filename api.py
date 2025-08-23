import random
from flask import Flask, request
from split import split_text
from embed_and_store import add_documents
from summarize import summarize, metasum
from manage_documents import delete_docs, list_docs
import os
from emergency_delete import burn_evidence, burn_everything

app = Flask(__name__)

# Endpoint to handle new document uploads
@app.route('/new', methods=['POST'])
def handle_upload():
    body = request.get_json()
    user_id = body.get('user_id')
    notebook_id = body.get('notebook_id')
    doc_id = body.get('doc_id')
    text = body.get('text')
    
    # Validate request body
    if not user_id or not notebook_id or not doc_id or not text:
        return { "error": 'Bad request' }, 400
    
    # Generate summary, key topics, and title for the text
    summary, key_topics, title = summarize(text)
    
    # Split the text into smaller chunks and store embeddings
    splits = split_text(text, user_id, doc_id, notebook_id)
    embedding_ids = add_documents(splits)
    
    # Return the generated summary, topics, and title
    return {
        "summary": summary,
        "topics": key_topics,
        "title": title
    }, 200

# Endpoint to list document chunk IDs
@app.route('/list-docs', methods=['POST'])
def get_chunk_ids():
    body = request.get_json()
    doc_id = body.get('doc_id')

    # Validate request body
    if not doc_id:
        return { "error": 'Bad request' }, 400
    
    # Return the list of chunk IDs for the given document
    return { "ids": list_docs(doc_id) }

# Endpoint to delete document chunks by document ID
@app.route('/delete', methods=['POST'])
def delete_chunks_by_doc_id():
    body = request.get_json()
    doc_id = body.get('doc_id')

    # Validate request body
    if not doc_id:
        return { "error": 'Bad request' }, 400
    
    # Delete the document chunks and return success status
    return { "success": delete_docs(doc_id) }

# Endpoint to generate a meta-summary from multiple summaries
@app.route('/sum', methods=['POST'])
def handle_reupload():
    body = request.get_json()
    summaries = body.get('summaries')
    
    # Validate request body
    if not summaries:
        return { "error": 'Bad request' }, 400

    # Generate a meta-summary from the provided summaries
    metasummary = metasum(summaries)

    return metasummary, 200

# Endpoint to burn evidence (delete sensitive data)
@app.route('/burn evidence', methods=['POST'])
def destroy():
    burn_evidence()
    return { "success": "Evidence burned" }

# Endpoint to burn everything (delete all data)
@app.route('/burn everything', methods=['POST'])
def destroy_all():
    burn_everything()
    return { "success": "Everything burned" }

# Entry point for the Flask application
if __name__ == '__main__':
    # Check if the app is running in production mode
    if os.environ.get('FLASK_ENV') == 'production':
        print('Flask app ready for WSGI server in production')
    else:
        # Run the app in debug mode for development
        app.run(debug=True)
