from langchain_groq import ChatGroq

from config.settings import GROQ_API_KEY
from config.settings import GROQ_MODEL


class GroqService:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_MODEL,
            temperature=0
        )

    def get_llm(self):

        return self.llm