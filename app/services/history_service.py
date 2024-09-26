from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao import HistoryDAO

class HistoryService:
    def __init__(self, db: AsyncSession):
        self.dao = HistoryDAO(db)

    async def save_history(self, user_id: int, query: str, response: str):
        return await self.dao.create_history(user_id, query, response)

    async def get_user_history(self, user_id: int):
        return await self.dao.get_user_history(user_id)
