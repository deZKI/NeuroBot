from fastapi import FastAPI
from sqladmin import Admin

from app.admin.routes import UserAdmin, KnowledgeAdmin, HistoryAdmin
from app.bot.bot import start_bot
from app.db import engine, init_db
from app.neural.neural import NeuralNetwork

app = FastAPI()

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(KnowledgeAdmin)
admin.add_view(HistoryAdmin)

NNetwork = NeuralNetwork()

# Инициализация базы данных
@app.on_event("startup")
async def startup():
    await init_db()
    await start_bot()


@app.get("/")
async def root():
    return {"message": "NeuroBot API is running."}
