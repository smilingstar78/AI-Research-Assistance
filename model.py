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
# file_path = r"C:\Users\Dell\Downloads\_OceanofPDF.com_Atomic_Habits_-_James_Clear.pdf"

uploaded_file = st.file_uploader('Upload a file', type=['pdf'])
if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path = temp_file.name
    # reader = PdfReader(file_path)

    # text = ""
    # for page in reader.pages:
    #     text+=page.extract_text()

    # st.write(text[:1000])

    # doc = Document(page_content=text)

    loader = PyPDFLoader(temp_path)
    file = loader.load()

    embeddings_model = HuggingFaceEmbeddings(
        model_name = 'BAAI/bge-small-en-v1.5'
    )

    chunks = SemanticChunker(embeddings_model)

    # docs1 = embeddings_model.create_documents([file])

    docs = chunks.split_documents(file)

    # st.write(docs[0].page_content)

    chroma = Chroma(
        collection_name = 'documents',
        embedding_function = embeddings_model,
        persist_directory= "./chroma_db"
   )

    chroma.add_documents(docs)

    retriever = chroma.as_retriever(search_kwargs={'k':5})

    # st.subheader("Retrieved Chunks")


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

    llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),model='llama-3.3-70b-versatile')

    chain = prompt | llm | parser

    if "message_history" not in st.session_state:
        st.session_state.message_history = []

    query = st.chat_input('Ask me anything....')
    st.write("Query:", query)

    if query:
        st.session_state.message_history.append(HumanMessage(content=query))
        results = retriever.invoke(query)

        # for i, doc in enumerate(results):
        #     st.write(f"### Chunk {i+1}")
        #     st.write(doc.page_content)
        #     st.divider()
        
        content = []

        for i, doc in enumerate(results):
            content.append(doc.page_content)

        doc_content = "\n".join(content)

        result = chain.invoke({
            'query': message_history,
            'doc_content':doc_content
        })
        st.session_state.message_history.append(HumanMessage(content=query))
        st.write(result)

    # user_input = st.chat_input('Ask me anything....')

    # while True:
    # # if user_input:
    #     result = chain.invoke(input('User: '))
    #     print('ChatBot: ', result)

        # st.write(result)

