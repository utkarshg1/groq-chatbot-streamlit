# 🧠 Groq LLM Chat App

A simple interactive chatbot built with **Streamlit**, **LangChain**, and **Groq API**, allowing you to select LLM models and chat with them in real time.

---

### 🚀 Features

- Chat with Groq-hosted LLMs (e.g., LLaMA3, Mixtral)
- Select from available models dynamically
- Real-time streaming responses
- Session-persistent chat history
- Containerized with Docker

---

### 📁 Project Structure

```
.
├── app.py             # Main Streamlit app
├── models.py          # Model API + response logic
├── Dockerfile         # Container setup
├── docker-compose.yml # Optional: Docker orchestration
├── .env               # Environment variables (not committed)
└── README.md          # You're here!
```

---

### 🔧 Requirements

- Python 3.9+
- A valid [Groq API Key](https://console.groq.com/)
- A `MODELS_URL` endpoint (usually `https://api.groq.com/openai/v1/models`)

---

### 📦 Installation (Local)

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/groq-llm-chat.git
   cd groq-llm-chat
   ```

2. **Create `.env` file:**

   ```env
   GROQ_API_KEY=your_groq_api_key
   MODELS_URL=https://api.groq.com/openai/v1/models
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

### 🐳 Docker Usage

#### 1. **Build and run with Docker Compose:**

```bash
docker-compose up --build
```

Make sure your `.env` file is in the same directory. It will be automatically loaded by Compose.

#### 2. **Access the app:**

Go to [http://localhost:8501](http://localhost:8501) in your browser.

---

### 🧪 Example `.env`

```env
GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
MODELS_URL=https://api.groq.com/openai/v1/models
```

---

### 📌 Notes

- Make sure your Groq API key is active and has access to the model endpoints.
- Model switching is persistent and won't reset your chat unless you manually clear session state.

---

### 📜 License

MIT — free to use and modify.

---

### 👨‍💻 Author

Built by **Utkarsh Gaikwad**
Inspired by the power of LLMs and lightweight UIs.
