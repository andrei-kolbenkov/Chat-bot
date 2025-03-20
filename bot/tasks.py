from celery import Celery
from aiogram import Bot
import asyncio
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Создаем Celery приложение
celery = Celery('tasks', broker='redis://redis:6379/0')

# Асинхронная функция для отправки сообщения
async def delayed_send(chat_id, text):
    await asyncio.sleep(10) # Ждем 10 секунд
    await bot.send_message(chat_id, text) # Отправляем текст обратно пользователю

# Celery задача
@celery.task
async def delayed_echo_task(chat_id: int, text: str):
    await delayed_send(chat_id, text)