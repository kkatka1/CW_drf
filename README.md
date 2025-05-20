#  Habit Tracker Backend (Django + DRF)

Этот проект — серверная часть трекера полезных привычек, вдохновлённого книгой «Атомные привычки» Джеймса Клира. 

##  Возможности

-  Регистрация и авторизация пользователей (JWT)
-  Создание, просмотр, редактирование, удаление привычек
-  Привязка приятных привычек и вознаграждений
-  Публичные привычки доступны всем
-  Покрытие тестами > 80%
-  Стиль кода соответствует PEP8 (flake8 100%)
-  Интеграция с Telegram
-  Напоминания через Celery + Beat
-  Документация Swagger / ReDoc

---

##  Установка и запуск

```bash
git clone https://github.com/your-username/habit-tracker-backend.git
cd habit-tracker-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Создайте файл `.env` и добавьте:

```env
SECRET_KEY=your-secret-key
DB_NAME=cw_drf
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
TELEGRAM_TOKEN=your-bot-token
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

Примените миграции:
```bash
python manage.py migrate
```

Создайте суперпользователя:
```bash
python manage.py csu
```

Запустите сервер:
```bash
python manage.py runserver
```

---

##  Celery + Telegram

### Запуск Celery worker:
```bash
celery -A config worker -l info
```

### Запуск Beat:
```bash
celery -A config beat -l info
```

---

##  Интеграция с Telegram

- Создайте бота через [@BotFather](https://t.me/BotFather)
- Сохраните токен в `.env` как `TELEGRAM_TOKEN`
- Установите `tg_chat_id` пользователя вручную через `/admin`

---

##  Документация

- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

##  Тестирование

Покрытие:
```bash
coverage run manage.py test
coverage report > coverage.txt
```

Тестовое покрытие: **86%**  
См. [`coverage.txt`](./coverage.txt)

---

##  Flake8

```bash
flake8 . > flake8_report.txt
```

 Код проходит flake8 со стилем 100%  
См. [`flake8_report.txt`](./flake8_report.txt)

---

##  Примеры

###  Регистрация:
POST `/users/register/`
```json
{
  "email": "user@example.com",
  "password": "123qwe456rty",
  "first_name": " ",
  "last_name": " "
}
```

###  Получение токена:
POST `/users/login/`
```json
{
  "email": "user@example.com",
  "password": "123qwe456rty"
}
```

###  Создание привычки:
```json
{
  "place": "Дом",
  "time": "15:00:00",
  "action": "Чтение книги",
  "execution_time": 120,
  "periodicity": 1,
  "is_public": true,
  "is_pleasant": false
}
```

###  Публичные привычки:
GET `/habits/public/` (без авторизации)
