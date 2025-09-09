# Loads PDFs, vector DB, embeddings, QA chain

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from app.core.config import settings
import os

# --- Step 1: Load PDFs ---
docs = []
for path in settings.PDF_PATHS:
    if os.path.exists(path):
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

# --- Step 2: Split ---
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# --- Step 3: Vector DB ---
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=settings.VECTORDB_PATH)
vectordb.persist()

# --- Step 4: Groq LLM ---
llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0, groq_api_key=settings.GROQ_API_KEY)

# --- Step 5: Chain ---
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(),
    memory=memory
)
