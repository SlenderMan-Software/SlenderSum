![Alt text](logo.png)

# SlenderSum, text embedder and summarizer API

This project is a text embedding and storage system that processes text documents, splits them into smaller chunks, generates embeddings for each chunk, and stores them in a vector database. It also includes an API for uploading and processing new documents. It also uses Gemini to summarize your upload.

## Features

- **Text Splitting**: Splits large text documents into smaller chunks using a recursive character text splitter.
- **Text Embedding**: Generates embeddings for text chunks using Google Generative AI Embeddings.
- **Vector Storage**: Stores embeddings in a Chroma vector database for efficient retrieval.
- **API**: Provides a Flask-based API for uploading and processing new documents.
- **Testing Scripts**: Includes scripts for testing text splitting, embedding, and API functionality.
- **Summarization**: Asks Google Gemini to summarize your source

## Project Structure

- **`api.py`**: Flask API for handling document uploads and processing, and summarizing.
- **`embed_and_store.py`**: Handles embedding generation and storage in the Chroma vector database.
- **`split.py`**: Contains the logic for splitting text into smaller chunks.
- **`text_split.py`**: A script for testing text splitting and embedding functionality.
- **`post.py`**: A script for testing the API by sending a sample document.
- **`summarize.py`**: Contains function for sending summary, title, and key-topics request to Gemini, parses them for API.
## Downloads
Get the latest release from [Releases](https://github.com/SlenderMan-Software/SlenderSum/releases).


## Setup
- **Automatic**
  - To install automatically, download the installer for your operating system, run it, and provide your API key.
- **Manual**
- Clone this repository using
  ```sh
  git clone https://github.com/GrinchBob43/SlenderSum.git
  cd SlenderSum
  ```
- create a .env file with
  ```sh
  nano .env
  ```
  Then set variable ```GOOGLE_API_KEY='<My google developer API key>'```
  Then use ```Ctrl + X``` to exit and save
- Install dependencies with:
  ```sh
  pip install -r requirements.txt
  ```
- Run the API with
  ```sh
  python3 api.py
  ```

## Usage
- Sending a POST request to the **/new** endpoint with the correct json payload will return generate embeddings for the text that are stored in the chroma database. It will then generate a summary of the text, along with a suggested title and some key topics (WIP)
 
## Testing the API
Run the post.py script to test the API
Testing Text Splitting and Embedding:
  Run the text_split.py script to test text splitting and embedding functionality.
 

## Adding New Documents
Send a POST request to the /new endpoint of the API with the following metadata:

{
  "text": "<your-text>",
  "doc_id": "<document-id>",
  "user_id": "<user-id>",
  "notebook_id": "<notebook-id>"
}

- A successfull response will look something like this:
```
Request successful!
{'summary': 'summary', 'title': 'title', 'topics': [topic_A, topic_b, etc]}
```

- If you don't include one of the parameters in your json payload you will get an error like this:
```
{
  Error: 400
{
  "error": "Bad request"
}
}
```
## Notes
The Chroma vector database is stored in the chroma_langchain_db/ directory.
Ensure that the chroma_langchain_db/ directory is writable for the application.
