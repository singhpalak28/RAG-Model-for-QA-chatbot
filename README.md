# Retrieval-Augmented Generation (RAG) QA Bot

This project implements a Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot. The bot can answer questions based on uploaded documents by leveraging a vector database(Pinecone) for retrieval and a generative model(Cohere) for generating coherent responses. The application is built with a simple frontend interface using Gradio.

## Project Overview
The project consists of two main parts:
1. **Part 1: RAG Model for QA Bot**
   - Implemented a Retrieval-Augmented Generation (RAG) model using a vector database(Pinecone) and a generative model(Cohere API).
   - The model is able to retrieve relevant information from a dataset and generate coherent answers.

2. **Part 2: Interactive QA Bot Interface**
   - Built an interactive interface using Gradio where users can upload PDF documents and ask questions.
   - The system allows users to input queries and retrieve answers in real time. It also enables users to upload documents and ask questions based on the content of the uploaded document.
     
## Features
- Upload PDF documents and ask questions about the content.
- Real-time responses based on document content.
- Uses a vector database for efficient document retrieval.
- Displays retrieved document segments alongside the generated answers.
- Supports multiple queries with minimal performance degradation.

## Architecture
The architecture consists of:
1. **Frontend (Gradio):** Enables users to upload documents and interact with the QA bot.
2. **Backend (RAG Model):** Uses a vector database (e.g., Pinecone) for storing document embeddings and a generative model (e.g., Cohere API) for generating answers.
3. **Containerization (Docker):** The application is containerized using Docker for easy deployment and scaling.

## Getting Started
### Prerequisites
- Docker installed on your machine.
- Python 3.7+ and pip.
- (Optional) GPU for faster embedding and inference.

### Step-by-Step Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Set your environment variables: Create a .env file in the root directory and add your API keys:
   ```bash
   COHERE_API_KEY=your-cohere-api-key
   PINECONE_API_KEY=your-pinecone-api-key
   
5. Run the application:
   ```bash
    python app.py

### Running with Docker
To make it easier to run and deploy, the application is fully containerized. You can run the entire system using Docker.
   
1. Build the Docker container:
   ```bash
   docker build -t rag-qa-bot .

2. Run the Docker container:
   ```bash
   docker run -p 7860:7860 rag-qa-bot

3. Access the application:
Once the Docker container is running, you can access the interactive QA bot interface via your browser at 'http://localhost:7860'.

## Usage
**Upload a Document:**
  -Open the application in a web browser (http://localhost:7860).
  -Upload a PDF document.
**Ask Questions:**
  -Type a question in the provided input box.
  -The bot will retrieve relevant content from the uploaded document and generate a response.
**View Responses:**
  -The retrieved document segments will be displayed along with the generated answer.

## Project Structure
    '''bash
     .
    ├── .dockerignore          # Files to ignore during Docker build
    ├── Dockerfile             # Docker configuration file for containerizing the app
    ├── app.py                 # Frontend application (Gradio)
    ├── backend.py             # Backend logic for the RAG model
    ├── requirements.txt       # Python dependencies
    ├── RAG.ipynb              # Colab notebook demonstrating the entire RAG pipeline
    └── README.md              # Project documentation







