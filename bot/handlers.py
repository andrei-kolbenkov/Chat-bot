import logging
import asyncio
from aiogram import types

# Настройка логирования
logger = logging.getLogger(__name__)


# Обработчик команды /start
async def send_welcome(message: types.Message):
    # Берем данные для логирования
    user_id = message.from_user.id  # ID пользователя
    user_name = message.from_user.username  # @Username
    logger.info(f"{user_name} (ID: {user_id}) запустил бота.")

    welcome_text: str = "Добро пожаловать в бота! Отправьте сообщение, и оно вернется к вам через 10 секунд!"
    # Отправка сообщения пользователю
    await message.answer(welcome_text)


# Обработчик сообщений
async def echo_message(message: types.Message):
    # Берем данные для логирования
    user_id = message.from_user.id  # ID пользователя
    user_name = message.from_user.username  # @Username
    user_text: str = message.text  # Текст сообщения
    logger.info(f"{user_name} (ID: {user_id}) отправил сообщение: {user_text}")

    await asyncio.sleep(10)  # Ждем 10 секунд
    await message.answer(user_text)  # Отправляем текст обратно