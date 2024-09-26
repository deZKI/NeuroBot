from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User, History, Knowledge
from sqlalchemy.future import select


class UserDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_telegram_id(self, telegram_id: int):
        result = await self.db.execute(select(User).filter(User.telegram_id == telegram_id))
        return result.scalars().first()

    async def create_user(self, telegram_id: int, username: str, first_name: str, last_name: str):
        user = User(telegram_id=telegram_id, username=username, first_name=first_name, last_name=last_name)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user


class HistoryDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_history(self, user_id: int, query: str, response: str):
        history_entry = History(user_id=user_id, query=query, response=response)
        self.db.add(history_entry)
        await self.db.commit()
        await self.db.refresh(history_entry)
        return history_entry

    async def get_user_history(self, user_id: int):
        result = await self.db.execute(select(History).filter(History.user_id == user_id))
        return result.scalars().all()


class KnowledgeDAO:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_knowledge_by_query(self, query: str):
        result = await self.db.execute(select(Knowledge).filter(Knowledge.question == query))
        return result.scalars().first()

    async def create_knowledge(self, question: str, answer: str):
        knowledge_entry = Knowledge(question=question, answer=answer)
        self.db.add(knowledge_entry)
        await self.db.commit()
        await self.db.refresh(knowledge_entry)
        return knowledge_entry
