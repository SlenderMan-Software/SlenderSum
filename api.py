import random
from flask import Flask, request
from split import split_text
from embed_and_store import add_documents
from summarize import summarize
from manage_documents import delete_docs, list_docs
import os
from emergency_delete import burn_evidence, burn_everything

app = Flask(__name__)

@app.route('/new', methods=['POST'])
def handle_upload():
    body = request.get_json()
    user_id = body.get('user_id')
    notebook_id = body.get('notebook_id')
    doc_id = body.get('doc_id')
    text = body.get('text')
    

    if not user_id or not notebook_id or not doc_id or not text:
        return { "error": 'Bad request' }, 400
    summary, key_topics, title = summarize(text)
    splits = split_text(text, user_id, doc_id, notebook_id)
    embedding_ids = add_documents(splits)
    
    return {
        "summary": summary,
        "topics": key_topics,
        "title": title
    }, 200
    
#@app.route('/summarize', methods=['POST'])
 #   def write_this_soon(text):
  #  summary = summarize("This is a test")

@app.route('/list-docs', methods=['POST'])
def get_chunk_ids():
    body = request.get_json()
    doc_id = body.get('doc_id')

    if not doc_id:
        return { "error": 'Bad request' }, 400
    
    return { "ids": list_docs(doc_id) }

@app.route('/delete', methods=['POST'])
def delete_chunks_by_doc_id():
    body = request.get_json()
    doc_id = body.get('doc_id')

    if not doc_id:
        return { "error": 'Bad request' }, 400
    
    return { "success": delete_docs(doc_id) }

@app.route('/burn evidence', methods=['POST'])
def destroy():
    burn_evidence()
    return { "success": "Evidence burned" }

@app.route('/burn everything', methods=['POST'])
def destroy_all():
    burn_everything()
    return { "success": "Everything burned" }




if __name__ == '__main__':
     if os.environ.get('FLASK_ENV') == 'production':
        print('Flask app ready for WSGI server in production')
     else:
        app.run(debug=True)

