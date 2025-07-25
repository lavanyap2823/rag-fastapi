from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from typing import List
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
from chroma_utils import vectorstore

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

output_parser = StrOutputParser()


contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

# To reformulate the user's question based on chat history.
contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# To generate the final answer based on the retrieved context and chat history.
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Use the following context to answer the user's question."),
    ("system", "Context: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

def get_rag_chain(model="gpt-4o-mini"):
    llm = ChatOpenAI(model=model, api_key=OPENAI_API_KEY)
    
    #Create a history-aware retriever that can understand context from previous interactions.
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
    
    #Set up a question-answering chain that combines retrieved documents to generate an answer.
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    
    #create the full RAG chain by combining the retriever and question-answering chain.
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)    
    return rag_chain
