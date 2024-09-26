import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

async def test_connection():
    DATABASE_URL = "postgresql+asyncpg://neurobot:postgres@localhost/postgres"  # или "db", если в Docker
    engine = create_async_engine(DATABASE_URL, echo=True)

    async with engine.begin() as conn:
        print("Successfully connected to the database.")

asyncio.run(test_connection())
