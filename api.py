import random
from flask import Flask, request
from split import split_text
from embed_and_store import add_documents

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
    
    splits = split_text(text, user_id, doc_id, notebook_id)
    embedding_ids = add_documents(splits)
    return { "embedding_ids": embedding_ids }


if __name__ == '__main__':
    app.run(debug=True)

