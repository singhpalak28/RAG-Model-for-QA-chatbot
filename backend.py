import cohere
import pinecone
import PyPDF2
import os
from pinecone import Pinecone, ServerlessSpec
# Initialize Cohere
cohere_client = cohere.Client('SeiMH89JES2SBOmT811HSH9JC7kq9rc07pyTCqvT')
#docker run -p 7860:7860 --env COHERE_API_KEY=SeiMH89JES2SBOmT811HSH9JC7kq9rc07pyTCqvT --env PINECONE_API_KEY=db545199-08c0-4f4a-a285-79401be8375f rag-qa-bot


# Initialize Pinecone client
pc = Pinecone(api_key='db545199-08c0-4f4a-a285-79401be8375f')

# Define index name and dimension
index_name = 'qa-bot'

# Check if the index exists, create it if not
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=4096,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'  # Set the appropriate region
        )
    )

# Connect to the index
index = pc.Index(index_name)
# Function to read and extract text from PDF
def upload_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to ingest PDF text into Pinecone
def ingest_pdf(file):
    pdf_text = upload_pdf(file)

    # Split text into chunks if needed
    documents = pdf_text.split('\n\n')  # Adjust as needed for chunking

    # Create embeddings for each chunk
    embeddings = cohere_client.embed(texts=documents).embeddings

    # Insert embeddings into Pinecone
    for i, embed in enumerate(embeddings):
        index.upsert([(str(i), embed, {"text": documents[i]})])

    return "PDF content has been successfully ingested into Pinecone."

# Retrieve relevant documents based on a query
def retrieve_relevant_docs(query):
    query_vector = cohere_client.embed(texts=[query]).embeddings[0]
    response = index.query(
        vector=query_vector,
        top_k=5,
        include_values=True,
        include_metadata=True
    )
    retrieved_docs = [match['metadata'] for match in response['matches']]
    return retrieved_docs

# Generate answer based on the retrieved documents
def generate_answer(query, retrieved_docs):
    if retrieved_docs:
        context = ' '.join([doc['text'] for doc in retrieved_docs])
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nPlease provide a direct answer based on the context above:"
    else:
        prompt = f"Question: {query}\n\nPlease provide a direct answer based on your knowledge."

    response = cohere_client.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=100,
        temperature=0.5
    )
    return response.generations[0].text.strip()

# Combine document retrieval and answer generation
def qa_bot(query, pdf_file=None):
    if pdf_file is not None:
        # If a PDF is uploaded, ingest its content and retrieve relevant documents
        pdf_status = ingest_pdf(pdf_file)
        retrieved_docs = retrieve_relevant_docs(query)
        answer = generate_answer(query, retrieved_docs)
        return pdf_status, answer
    else:
        # If no PDF is uploaded, answer the question using general knowledge
        answer = generate_answer(query, [])
        return None, answer
