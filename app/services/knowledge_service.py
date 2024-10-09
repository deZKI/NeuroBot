from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao import KnowledgeDAO


class KnowledgeService:
    def __init__(self, db: AsyncSession):
        self.dao = KnowledgeDAO(db)

    async def get_answer(self, query: str):
        from app.main import NNetwork

        # Поиск ответа в базе знаний
        knowledge = await self.dao.get_knowledge_by_query(query)
        if knowledge:
            return knowledge.answer
        else:
            # Если ответ не найден, использовать нейросеть для генерации ответа
            response = NNetwork.generate_response(query)
            return response

    async def add_knowledge(self, question: str, answer: str):
        await self.dao.create_knowledge(question, answer)
