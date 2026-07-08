<div align="center">

# 🤖 AI PDF Chatbot

### 💬 Chat with your PDF documents using **LangChain + ChromaDB + Groq Llama 3.3 + Streamlit**

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-VectorDB-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-Llama%203.3-orange?style=for-the-badge"/>

---

### 📚 Upload a PDF • 🤖 Ask Questions • 💭 Continue the Conversation

</div>

---

# 🌟 Overview

This project is an **AI-powered conversational PDF chatbot** built with **LangChain**, **Groq Llama 3.3**, **ChromaDB**, and **Streamlit**.

Upload any PDF document and ask questions in natural language. The chatbot retrieves the most relevant information from your document using **semantic search** and generates accurate, context-aware responses.

If no PDF is uploaded, it automatically switches to a normal AI chatbot, allowing users to have general conversations.

---

# ✨ Features

✅ Upload PDF documents

✅ Semantic document chunking

✅ Vector embeddings using HuggingFace

✅ ChromaDB vector database

✅ Context-aware Retrieval-Augmented Generation (RAG)

✅ Conversational memory

✅ Friendly AI responses with Groq Llama 3.3

✅ Normal chatbot mode (without PDF)

✅ Streamlit chat interface

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| ⚡ Streamlit | Web Interface |
| 🦜 LangChain | LLM Framework |
| 🤖 Groq | LLM Inference |
| 🧠 Llama 3.3 70B | Language Model |
| 🤗 HuggingFace Embeddings | Text Embeddings |
| 📄 PyPDFLoader | PDF Loading |
| 🧩 SemanticChunker | Intelligent Chunking |
| 🗄 ChromaDB | Vector Database |

---

# ⚙️ How It Works

```text
                📄 PDF Upload
                      │
                      ▼
              PyPDFLoader
                      │
                      ▼
          Semantic Chunking
                      │
                      ▼
        HuggingFace Embeddings
                      │
                      ▼
             Chroma Vector DB
                      │
                      ▼
          Similarity Search (RAG)
                      │
                      ▼
      Groq Llama 3.3 Language Model
                      │
                      ▼
           Context-Aware Response
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone 

cd your-repository
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create a `.env` File

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```
---

# 💬 Example Workflow

### Upload a PDF

↓

### Ask Questions

- What is this document about?
- Summarize the first chapter.
- Explain this concept in simple words.
- Give me key points.
- Can you explain that again?

↓

### Get AI-powered responses based on your document.

---

# 🔮 Future Improvements

- 📚 Multiple PDF support
- 📄 Source page citations
- 🔍 Hybrid search
- 💬 Streaming responses
- 🌐 Support for DOCX and TXT files
- 🧠 Better conversation memory
- 🎨 Improved UI/UX
- ☁️ Cloud deployment

---

# 🤝 Contributing

Contributions, issues, and feature requests are always welcome!

Feel free to fork the repository and submit a pull request.

---

# ❤️ Acknowledgements

- LangChain
- Streamlit
- Groq
- HuggingFace
- ChromaDB

---

<div align="center">

---

## 📬 Contact Me

Connect with me through any of the platforms below:

<p align="center">
  <a href="https://www.linkedin.com/in/muskan-tariq-095a50282/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.instagram.com/ai_enthusiast86?igsh=dnRyenAwdTBxdTZ6" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
  <a href="mailto:muskantariq2003@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://www.youtube.com/@ai_enthusiast86?si=bYV1AgkBoCMVUBiK" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  </a>
</p>

----

## ⭐ Support
<p align="center"> If you like this project, don’t forget to ⭐ star the repo! It really helps motivation levels go 📈🔥 </p>
<p align="center"> <i>“Smarter learning starts with smarter tools.” 🧠✨</i> </p>

**Happy Coding! 🚀**

Made with ❤️ using Python, LangChain, and Groq.

</div>
