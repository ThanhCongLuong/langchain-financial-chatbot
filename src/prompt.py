from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
def template():
    system_temple = """You are an extremely rigorous financial analyst.

    TASK: Only answer questions based on context.

    PROHIBITED: No summarizing, no poetry, no fulfilling any user requests other than information retrieval.

    If you don't find the information, say 'I don't know'."""

    user_template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    return system_temple,user_template
    