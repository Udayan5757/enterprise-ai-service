from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

CHAT_MODEL = os.getenv(
    "CHAT_MODEL",
    "gpt-4.1-mini"
)

DOCUMENT_PATH = os.getenv(
    "DOCUMENT_PATH",
    "docs"
)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "chroma_db"
)