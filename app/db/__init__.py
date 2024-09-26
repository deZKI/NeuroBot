from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings
from app.db.models import Base

# Создание асинхронного движка базы данных
DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


# Функция для инициализации базы данных
async def init_db():
    async with engine.begin() as conn:
        # Создание всех таблиц в базе данных
        await conn.run_sync(Base.metadata.create_all)
