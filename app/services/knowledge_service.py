from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao import KnowledgeDAO
from app.neural.neural import NeuralNetwork


class KnowledgeService:
    def __init__(self, db: AsyncSession):
        self.dao = KnowledgeDAO(db)
        self.neural_network = NeuralNetwork()  # Инициализация нейросети

    async def get_answer(self, query: str):
        # Поиск ответа в базе знаний
        knowledge = await self.dao.get_knowledge_by_query(query)
        if knowledge:
            return knowledge.answer
        else:
            # Если ответ не найден, использовать нейросеть для генерации ответа
            response = self.neural_network.generate_response(query)
            return response
