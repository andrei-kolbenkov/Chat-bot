# Chat-bot

Этот проект представляет собой telegram-бот, который использует Celery и Redis для фоновых задач. Таким образом можно горизонтально масштабировать проект, путём увеличения количества воркеров, отдавая им задачи разного характера, которые занимают время. В коде присутствуют комментарии

## Структура проекта

- `bot/` - Основная директория с кодом бота.
  - `handlers.py` - Файл с обработчиками сообщений.
  - `main.py` - Основной файл для запуска бота.
  - `tasks.py` - Файл с задачами для Celery.
- `.env` - Файл с переменными окружения.
- `.gitignore` - Файл для исключения файлов из Git.
- `docker-compose.yml` - Файл для настройки и запуска контейнеров.
- `Dockerfile` - Файл для создания Docker-образа.
- `README.md` - Этот файл с инструкциями.
- `requirements.txt` - Файл с зависимостями Python.

## Установка и настройка

### Предварительные требования

- Установите Docker Desktop
- Установите Python версии 3.10 или выше
### Установка зависимостей

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/andrei-kolbenkov/Chat-bot.git
   cd Chat-bot
   
2. Создайте файл .env с переменной окружения для токена бота.
    ```BOT_TOKEN=token```
3. Установите зависимости 
   ```bash
   pip install -r requirements.txt

### Запуск через Docker

1. Соберите контейнеры
   ```bash
   docker-compose up --build
2. Основные команды:
   ```bash
   docker-compose up # Запуск
   docker-compose stop # Остановка
   docker-compose restart # Рестарт
   docker-compose ps # Просмотр контейнеров
   
### Запуск без Docker

1. Redis должен быть запущен локально
2. В терминале запустите воркер celery
    ```bash
   $env:CELERY_BROKER_URL = "redis://localhost:6379/0" # Если не получится, попробуйте изменить хост на другой 
   celery -A bot.tasks worker --loglevel=info --pool=solo # Запуск воркера
3. Запустите в терминале 
   ```bash
    cd bot
    python main.py