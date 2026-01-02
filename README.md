# 🍕 Pizza Restaurant Q&A Assistant

A Retrieval-Augmented Generation (RAG) system that answers questions about a pizza restaurant using customer reviews. This project uses LangChain, Ollama, and ChromaDB to create an intelligent Q&A assistant that can understand and respond to queries based on real customer feedback.

## 📋 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Example Questions](#example-questions)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **Semantic Search**: Uses vector embeddings to find the most relevant reviews for any question
- **Intelligent Responses**: Leverages LLM (Llama 3.2) to generate contextual answers based on customer reviews
- **Persistent Vector Database**: Stores embeddings in ChromaDB for fast retrieval
- **User-Friendly Interface**: Interactive command-line interface with clear formatting
- **Error Handling**: Robust error handling with helpful messages

## 🔧 How It Works

1. **Vector Database Creation**: 
   - Loads restaurant reviews from CSV file
   - Converts each review into a vector embedding using `mxbai-embed-large` model
   - Stores embeddings in ChromaDB for efficient similarity search

2. **Question Processing**:
   - User asks a question about the restaurant
   - System converts the question into a vector embedding
   - Finds the top 5 most similar reviews using cosine similarity

3. **Answer Generation**:
   - Retrieves relevant reviews with metadata (rating, date)
   - Sends reviews as context to Llama 3.2 LLM
   - Generates a comprehensive answer based on the retrieved reviews

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+**
- **Ollama** - [Download here](https://ollama.ai/)
- **Ollama Models**:
  - `llama3.2` - For text generation
  - `mxbai-embed-large` - For embeddings

### Installing Ollama Models

After installing Ollama, run these commands to download the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

## 🚀 Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd ttgg
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Ensure Ollama is running**:
   - Make sure Ollama service is running on your system
   - Verify models are installed: `ollama list`

## 💻 Usage

### Running the Application

Simply run the main script:

```bash
python main.py
```

Or use the provided run scripts:

- **Windows**: `run.bat` or `.\run.ps1`
- **Linux/Mac**: `python main.py`

### Interactive Session

Once the application starts, you'll see:

```
============================================================
🍕 Pizza Restaurant Q&A Assistant
============================================================
Ask me anything about the restaurant based on customer reviews!
Type 'q' or 'quit' to exit.

------------------------------------------------------------
❓ Your question: 
```

### Example Interaction

```
❓ Your question: What are the best pizza options?

🔍 Searching through reviews...
📚 Found 5 relevant review(s)

🤖 Generating answer...

------------------------------------------------------------
💬 Answer:
Based on the customer reviews, here are some of the best pizza options:

1. **Margherita Pizza** - Customers rave about the authentic Italian experience with wood-fired Margherita featuring perfect char, fresh basil, and buffalo mozzarella.

2. **Pepperoni Pizza** - The signature pepperoni pizza receives high praise for its perfect ratio of sauce to cheese, with pepperoni that curls into "little cups of deliciousness."

3. **Detroit-Style Pizza** - The square Detroit-style pizza is described as incredible with crispy cheese edges, fluffy interior, and perfect corner pieces.

4. **White Pizza** - The "White Album" pizza with ricotta, mozzarella, garlic, and spinach is phenomenal, especially with the spicy honey drizzle.

5. **Vegan Options** - The vegan pizza with cashew cheese is highly recommended, even by non-vegan customers.

The restaurant is known for using high-quality ingredients, including imported Italian flour, San Marzano tomatoes, and house-made mozzarella.
```

## 📁 Project Structure

```
ttgg/
│
├── main.py                          # Main application entry point
├── vector.py                        # Vector database setup and retrieval
├── realistic_restaurant_reviews.csv # Customer reviews dataset (124 reviews)
├── requirements.txt                 # Python dependencies
├── run.bat                          # Windows batch script to run the app
├── run.ps1                          # PowerShell script to run the app
├── README.md                        # This file
│
└── chrome_langchain_db/            # ChromaDB vector database (auto-created)
    ├── chroma.sqlite3
    └── [vector data files]
```

## ⚙️ Configuration

You can modify the following settings in `vector.py`:

```python
CSV_FILE = "realistic_restaurant_reviews.csv"  # Reviews data file
DB_LOCATION = "./chrome_langchain_db"           # Vector DB location
EMBEDDING_MODEL = "mxbai-embed-large"           # Embedding model
COLLECTION_NAME = "restaurant_reviews"          # ChromaDB collection name
NUM_RESULTS = 5                                 # Number of reviews to retrieve
```

In `main.py`, you can adjust:

```python
model = OllamaLLM(model="llama3.2", temperature=0.7)  # LLM model and temperature
```

## 🛠️ Technologies Used

- **[LangChain](https://www.langchain.com/)** - Framework for building LLM applications
- **[LangChain Ollama](https://python.langchain.com/docs/integrations/llms/ollama)** - Ollama integration for LangChain
- **[LangChain Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma)** - ChromaDB integration
- **[ChromaDB](https://www.trychroma.com/)** - Vector database for embeddings
- **[Ollama](https://ollama.ai/)** - Local LLM runtime
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **Llama 3.2** - Large Language Model for text generation
- **mxbai-embed-large** - Embedding model for vector search

## 💡 Example Questions

Try asking questions like:

- "What are the best pizza options?"
- "Is the restaurant good for families?"
- "What do customers say about the service?"
- "Are there gluten-free options?"
- "What are common complaints?"
- "What makes this restaurant special?"
- "Is the pizza expensive?"
- "What are the vegan options?"

## 🔍 Troubleshooting

### Ollama Connection Issues

**Error**: `Failed to initialize embeddings` or `Error initializing model`

**Solution**:
1. Ensure Ollama is running: Check if Ollama service is active
2. Verify models are installed: `ollama list`
3. Pull missing models: `ollama pull llama3.2` and `ollama pull mxbai-embed-large`

### Module Not Found Errors

**Error**: `ModuleNotFoundError: No module named 'langchain_ollama'`

**Solution**:
```bash
pip install -r requirements.txt
```

### Vector Database Issues

**Error**: Database corruption or missing files

**Solution**: Delete the `chrome_langchain_db` folder and restart the application. It will recreate the database automatically.

### Encoding Issues (Windows)

If you encounter encoding errors with Arabic characters in paths:

1. Use the provided `run.bat` or `run.ps1` scripts
2. Or set environment variable: `set PYTHONIOENCODING=utf-8`

## 📊 Dataset

The project includes `realistic_restaurant_reviews.csv` with 124 customer reviews containing:
- **Title**: Review title
- **Date**: Review date
- **Rating**: Star rating (1-5)
- **Review**: Full review text

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [Ollama](https://ollama.ai/) and local LLMs
- Vector database by [ChromaDB](https://www.trychroma.com/)

---

**Enjoy your Pizza Restaurant Q&A Assistant! 🍕**
