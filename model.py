from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pypdf import PdfReader
from langchain_core.documents import Document
import tempfile
from langchain_core.messages import HumanMessage, AIMessage

st.title('MY CHATBOT')

load_dotenv()

parser = StrOutputParser()

uploaded_file = st.file_uploader('Upload a file', type=['pdf'])

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "current_file" not in st.session_state:
    st.session_state.current_file = None

llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),model='llama-3.3-70b-versatile')

class Chatbot_with_file:

    def __init__(self, file, query):
        self.file = file
        self.query = query

    def file_operations(file):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.getvalue())
            temp_path = temp_file.name

        loader = PyPDFLoader(temp_path)
        file = loader.load()

        embeddings_model = HuggingFaceEmbeddings(
            model_name = 'BAAI/bge-small-en-v1.5'
        )

        chunks = SemanticChunker(embeddings_model)


        docs = chunks.split_documents(file)


        chroma = Chroma(
            collection_name = 'documents',
            embedding_function = embeddings_model,
            persist_directory= "./chroma_db"
    )
        chroma.reset_collection()

        chroma.add_documents(docs)

        retriever = chroma.as_retriever(search_kwargs={"k": 5})

        st.session_state.retriever = retriever

    def retrieve_content(retriever, query):

        prompt = ChatPromptTemplate.from_messages([
        ("system",
        """You are a helpful assistant.
        Use the given context to answer the user's question.
        Be friendly and use emojis.

        Context:
        {doc_content}
        """),

        MessagesPlaceholder(variable_name="chat_history"),

        ("human", "{query}")
        ])
        st.session_state.message_history.append(HumanMessage(content=query))
        history = ""

        for msg in st.session_state.message_history:
            history += msg.content + "\n"

        search_query = history + "\n" + query

        results = retriever.invoke(search_query)
        
        content = []

        for i, doc in enumerate(results):
            content.append(doc.page_content)

        doc_content = "\n".join(content)

        chain = prompt | llm | parser

        result = chain.invoke({
        'query': query,
        'doc_content': doc_content,
        'chat_history': st.session_state.message_history
    })

        st.session_state.message_history.append(
            AIMessage(content=result)
        )

        with st.chat_message("assistant"):
            st.write(result)

class Chatbot_no_file:
    def __init__(self, query):
        self.query = query
    def chat(query):
        prompt = ChatPromptTemplate.from_messages([
        ("system",
        """You are a helpful assistant.
        Talk very friednly. Use emojis.
        """),

        MessagesPlaceholder(variable_name="chat_history"),

        ("human", "{query}")
        ])
        chain = prompt | llm | parser
        result = chain.invoke({
            'query':query,
            'chat_history': st.session_state.message_history
        })
        st.session_state.message_history.append(
            AIMessage(content=result)
        )

        with st.chat_message("assistant"):
            st.write(result)

if "message_history" not in st.session_state:
     st.session_state.message_history = []

if uploaded_file is not None:

    if st.session_state.current_file != uploaded_file.name:

        Chatbot_with_file.file_operations(uploaded_file)

        st.session_state.current_file = uploaded_file.name
    # Chatbot_with_file.file_operations(uploaded_file)
    # answer = Chatbot_with_file.file_operations(uploaded_file)

for message in st.session_state.message_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)
            # st.markdown(message.content)

query = st.chat_input('Ask me anything....')

if query:
    st.session_state.message_history.append(
        HumanMessage(content=query)
    )

    with st.chat_message("user"):
        st.markdown(query)
    if st.session_state.retriever is not None:
        Chatbot_with_file.retrieve_content(
            st.session_state.retriever,
            query
        )
    else:
        Chatbot_no_file.chat(query)