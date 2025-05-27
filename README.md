# RAG Chatbot with FastAPI and Langchain

## Overview
This project demonstrates how to build a production-ready Retrieval-Augmented Generation (RAG) chatbot using Langchain. The chatbot can answer questions based on documents uploaded by the user. This project covers the entire process from document loading and processing to retrieval and response generation.

### Features

- **Chat Functionality**: The chatbot processes user questions and maintains context through a session ID, enabling follow-up questions.
- **Document Management**:
  - Upload documents for the chatbot to reference.
  - List documents and their details in the system.
  - Delete documents and their associated indexed data.
- **Structured Input and Output**: The application uses Pydantic models to define the structure for both incoming queries and outgoing responses, ensuring clear and consistent data handling.
- **Database Integration**: Uses a database to maintain chat logs and document records.


## Getting Started

### Prerequisites
- Python 3.7 or higher
- Necessary libraries included in `requirements.txt`
- Access to a compatible LLM (e.g., OpenAI API)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lavanyap2823/rag-fastapi.git
   cd rag-fastapi
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
### Project Structure

- `main.py`: The entry point for the FastAPI application; defines API endpoints.
- `db_utils.py`: Contains utility functions for handling database operations and chat history.
- `chroma_utils.py`: Manages vector search related tasks such as indexing and splitting documents.
- `pydantic_models.py`: Defines Pydantic models for input and output schemas.

### Code Snippets
#### Loading and Processing Documents
```python
from langchain.document_loaders import PDFLoader, DocxLoader

# Load and split documents
def load_documents(folder_path):
    # Implementation to load and process documents
    pass
```

#### Creating the Vector Store
```python
from langchain.vectorstores import Chromadb

# Create and store document embeddings in the vector store
vector_store = Chromadb()
```

#### Retrieving Answers
```python
# Define the process of retrieving relevant documents and generating responses
def query_chatbot(question):
    # Logic to query the vector store and generate a response using the LLM
    pass
```

### API Endpoints

1. **Chat Endpoint**: Processes user queries and returns appropriate responses.
2. **Upload Document Endpoint**: Accepts file uploads and indexes them.
3. **List Documents Endpoint**: Returns a list of uploaded documents.
4. **Delete Document Endpoint**: Deletes specified documents and their related indexed data.

### Running the Application

To run the API server:

```bash
uvicorn main:app --reload
```

## Conclusion
This project provides a comprehensive guide to building a RAG chatbot using Langchain. By following the steps outlined in this README, you can implement a fully functioning chatbot capable of utilizing external documents to provide informative answers.

---

Happy Coding!
