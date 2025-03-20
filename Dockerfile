FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY bot ./bot

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Стартовая команда
CMD ["python", "bot/main.py"]
