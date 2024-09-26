from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dao import UserDAO

class UserService:
    def __init__(self, db: AsyncSession):
        self.dao = UserDAO(db)

    async def get_or_create_user(self, telegram_id: int, username: str, first_name: str, last_name: str):
        user = await self.dao.get_user_by_telegram_id(telegram_id)
        if not user:
            user = await self.dao.create_user(telegram_id, username, first_name, last_name)
        return user
