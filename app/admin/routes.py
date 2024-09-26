from sqladmin import ModelView
from app.db.models import User, Knowledge, History


# Настройка модели для пользователя
class UserAdmin(ModelView, model=User):
    pass


# Настройка модели для знаний
class KnowledgeAdmin(ModelView, model=Knowledge):
    pass


# Настройка модели для истории
class HistoryAdmin(ModelView, model=History):
    pass
