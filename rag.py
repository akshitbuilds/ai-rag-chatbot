from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

def create_vector_db(text):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(docs, embeddings)

    return db