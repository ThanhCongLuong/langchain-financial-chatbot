from src.data_utils import *
from src.config import *
from src.retrievers import *
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.prompt import template
import gradio as gr
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import pickle
import os

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING)
index = check_index(INDEX_FILE,embeddings)
if index is None:
    output_path = export_many_files(INPUT_PATH,OUTPUT_PATH)
    all_chunks = extract_chunk(output_path)
    save_chunks(CHUNKS_FILE,all_chunks)
    index = context_retriever(all_chunks,embeddings)
    save_index(index,INDEX_FILE)
else:
    with open(CHUNKS_FILE, "rb") as f:
        all_chunks = pickle.load(f)
retriever = index.as_retriever(search_kwargs={'k':5})
bm25 = bm25_retriever(all_chunks)
hybrid_retriever = hybrid_retriever(retriever,bm25)

llm = ChatGroq(model=MODEL_NAME,api_key=API_KEY)
system_tmp, user_tmp = template()
prompt = ChatPromptTemplate.from_messages([
    ('system',system_tmp),
    ('user',user_tmp)
])
chain = (
    {"context": hybrid_retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
def ques_ans(message, history):
    docs = hybrid_retriever.invoke(message)    
    full_answer = ""
    for chunk in chain.stream(message):
        full_answer += chunk
        yield full_answer

if __name__ == "__main__":
    demo = gr.ChatInterface(
    fn=ques_ans, 
    title="Financial AI Assistant",
    description="Please ask me everything about the annual report of Shopify",
    examples=["What was the revenue of Shopify in 2024?", "List the main risk factors."],
    )
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)


