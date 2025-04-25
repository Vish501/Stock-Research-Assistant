import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.url import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv


# Loading Google API Key
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.environ.get("GENAI_API_KEY")

# Initializing LLM from Google
def llm_construct():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17",
        temperature=0,
        max_retries=2,
    )

# Initializing embdeddings model
def embeddings_construct():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Loading data and creating vector
def data_loader(urls: list, embeddings):
    # Creating splitter
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

    # Loading data from provided urls
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    # Creating chunks
    chunks = splitter.split_documents(data)

    # Creating vector index
    return FAISS.from_documents(chunks, embeddings)

# Creating retrieval chain
def retrieval_construct(llm, vector_index):
    return RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_index.as_retriever())