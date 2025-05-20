from celery import shared_task
from django.utils import timezone

from .models import Habit
from .services import send_telegram_message


@shared_task
def send_reminders_task():
    now = timezone.localtime()
    current_time = now.time()

    habits = Habit.objects.filter(
        time__hour=current_time.hour, time__minute=current_time.minute
    )

    for habit in habits:
        if habit.user.tg_chat_id:
            message = f"🔔 Напоминание: {habit.action} в {habit.time.strftime('%H:%M')} на {habit.place}"
            send_telegram_message(message, habit.user.tg_chat_id)
