import requests
from config import settings


def send_telegram_message(message: str, chat_id: int):
    """
    Отправка сообщения в Telegram
    """
    url = f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage"

    params = {"chat_id": chat_id, "text": message}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
