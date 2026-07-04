from src.chains.rag_chain import RAGChain
from src.context.context_builder import ContextBuilder
from src.retrieval.retriever import RetrieverService


class ChatService:

    def __init__(self):

        self.retriever = RetrieverService()

        self.rag_chain = RAGChain()

    def ask(self, question: str):

        documents = self.retriever.retrieve_documents(question)

        context, sources = ContextBuilder.build(documents)

        answer = self.rag_chain.invoke(
            context=context,
            question=question
        )

        return {
            "answer": answer,
            "sources": sources
        }