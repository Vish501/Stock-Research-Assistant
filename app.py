import os
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Loading Google API Key
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.environ.get("GENAI_API_KEY")

# Initializing LLM from Google
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-preview-04-17",
    temperature=0,
    max_retries=2,
)

def main():
    st.title("Equity Research Tool 📈")
    st.sidebar.title("News Article URLs")



if __name__ == '__main__':
    main()