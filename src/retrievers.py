from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
import pickle

import os
def context_retriever(all_chunks,embeddings):
    index = FAISS.from_documents(all_chunks,embeddings)
    return index

def bm25_retriever(all_chunks):
    bm25 = BM25Retriever.from_documents(all_chunks)
    bm25.k = 5
    return bm25

def hybrid_retriever(retriever,bm25):
    hybrid_retriever = EnsembleRetriever(
        retrievers=[retriever,bm25],
        weights=[0.6,0.4])
    return hybrid_retriever

def save_index(retriever, path):
    retriever.save_local(str(path))
    print(f"Saved FAISS index to {path}")

def check_index(path,embeddings):
    if os.path.exists(path):
        print(f"Loading FAISS index from {path}...")
        return FAISS.load_local(str(path),embeddings,allow_dangerous_deserialization=True)
    else:
        return None
def save_chunks(path,chunks):
    with open(path, "wb") as f:
        pickle.dump(chunks, f)
