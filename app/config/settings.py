import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str = os.getenv("TELEGRAM_TOKEN")
    database_url: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"  # файл .env для загрузки переменных окружения


settings = Settings()
