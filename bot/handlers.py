import logging
import asyncio
from aiogram import types
from tasks import delayed_echo_task

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

    # Как пример, выносим задачу отдельно в celery и redis.
    # Таким образом любые задачи можно распределять по серверам для уменьшения нагрузки
    await delayed_echo_task(user_id, user_text)