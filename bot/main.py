import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from handlers import send_welcome, echo_message  # Импортируем хэндлеры


# Получаем токен бота из переменной окружения
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  # Формат логов
)
logger = logging.getLogger(__name__)


# Регистрируем хэндлеры
dp.message.register(send_welcome, Command("start"))
dp.message.register(echo_message)


# Главная функция запуска
async def main():
    try:
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())