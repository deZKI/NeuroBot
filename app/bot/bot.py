import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from app.config.settings import settings
from app.bot.keyboards import get_main_keyboard
from app.services.user_service import UserService
from app.services.knowledge_service import KnowledgeService
from app.services.history_service import HistoryService
from app.db import SessionLocal

bot = Bot(token=settings.telegram_token)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот с нейросетью и базой знаний. Выбери действие:", reply_markup=get_main_keyboard())


@dp.message()
async def message_handler(message: types.Message):
    async with SessionLocal() as db:
        user_service = UserService(db)
        knowledge_service = KnowledgeService(db)
        history_service = HistoryService(db)

        # Создаем или получаем пользователя
        user = await user_service.get_or_create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

        knowledge_answer = await knowledge_service.get_answer(message.text)

        # Сохраняем историю запроса
        await history_service.save_history(user_id=user.id, query=message.text, response=knowledge_answer)

        await message.reply(f"Ответ: {knowledge_answer}")


@dp.message(Command(commands=["history"]))
async def history_handler(message: types.Message):
    async with SessionLocal() as db:
        history_service = HistoryService(db)
        user_service = UserService(db)

        user = await user_service.get_or_create_user(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )

        history = await history_service.get_user_history(user.id)

        if history:
            history_messages = [f"Запрос: {h.query} | Ответ: {h.response} | Время: {h.timestamp}" for h in history]
            await message.reply("\n\n".join(history_messages))
        else:
            await message.reply("История запросов пуста.")


@dp.message(Command(commands=["add_knowledge"]))
async def add_knowledge_handler(message: types.Message):
    await message.reply(
        "Введите вопрос и ответ через разделитель '|'. Пример: 'Что такое AI?|AI - это искусственный интеллект.'")


@dp.message()
async def add_knowledge_process(message: types.Message):
    if '|' in message.text:
        question, answer = message.text.split('|', 1)
        async with SessionLocal() as db:
            knowledge_service = KnowledgeService(db)
            await knowledge_service.add_knowledge(question.strip(), answer.strip())
            await message.reply("Знание добавлено.")
    else:
        await message.reply("Неправильный формат. Введите вопрос и ответ через разделитель '|'.")


async def start_bot():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
