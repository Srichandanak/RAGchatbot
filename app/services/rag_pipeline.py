# Loads PDFs, vector DB, embeddings, QA chain
# app/services/rag_pipeline.py
# Loads PDFs, vector DB, embeddings, QA chain

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from app.core.config import settings
import os

# --- Step 1: Embeddings & VectorDB ---
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

vectordb = Chroma(persist_directory=settings.VECTORDB_PATH, embedding_function=embeddings)

# --- Step 2: LLM ---
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    groq_api_key=settings.GROQ_API_KEY
)

# --- Step 3: QA chain builder ---
qa_chain = None

def build_qa_chain():
    """Rebuild the QA chain with updated retriever."""
    global qa_chain
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectordb.as_retriever()
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

# --- Step 4: Ingestion ---
def ingest_document(file_path: str):
    """Load a new PDF and add to the vectorstore."""
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    vectordb.add_documents(chunks)
    vectordb.persist()

    # 🔄 Refresh chain with new retriever
    build_qa_chain()

# --- Initialize chain at startup ---
build_qa_chain()
