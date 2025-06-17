# Habit Tracker Backend (Django + DRF)

Этот проект — серверная часть трекера полезных привычек, вдохновлённого книгой «Атомные привычки» Джеймса Клира. 

## Возможности

- Регистрация и авторизация пользователей (JWT)
- Создание, просмотр, редактирование, удаление привычек
- Привязка приятных привычек и вознаграждений
- Публичные привычки доступны всем
- Покрытие тестами > 80%
- Стиль кода соответствует PEP8 (flake8 100%)
- Интеграция с Telegram
- Напоминания через Celery + Beat
- Документация Swagger / ReDoc

---

## Установка и запуск

```bash
git clone https://github.com/your-username/habit-tracker-backend.git
cd habit-tracker-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Создайте файл .env и добавьте:

SECRET_KEY=your-secret-key
DB_NAME=cw_drf
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
TELEGRAM_TOKEN=your-bot-token
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

Примените миграции:

python manage.py migrate

Создайте суперпользователя:

python manage.py csu

Запустите сервер:

python manage.py runserver

Docker
Локальный запуск:

docker compose up --build

Доступ:

    Backend: http://localhost:8080

    Swagger: http://localhost:8080/swagger/

    Admin: http://localhost:8080/admin/

Продакшн-сборка:

docker compose -f docker-compose.prod.yaml up --build -d

Доступ:

    NGINX проксирует на http://localhost:8080

CI/CD GitHub Actions

    Линтинг с flake8

    Тестирование с coverage

    Сборка и пуш Docker-образа

    Автодеплой на сервер по SSH

Добавьте в Secrets репозитория:

    SECRET_KEY

    DOCKER_USERNAME

    DOCKER_PASSWORD

    SSH_USER

    SSH_KEY

    SERVER_IP

Celery + Telegram

celery -A config worker -l info
celery -A config beat -l info

Swagger / Redoc

    Swagger: http://localhost:8080/swagger/

    Redoc: http://localhost:8080/redoc/