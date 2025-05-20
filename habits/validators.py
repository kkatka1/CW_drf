from rest_framework.exceptions import ValidationError


def validate_reward_and_related(reward, related_habit):
    if reward and related_habit:
        raise ValidationError(
            "Нельзя указывать и награду, и связанную приятную привычку."
        )


def validate_pleasant_habit(is_pleasant, reward, related_habit):
    if is_pleasant:
        if reward:
            raise ValidationError("Приятная привычка не может иметь награду.")
        if related_habit:
            raise ValidationError(
                "Приятная привычка не может иметь связанную привычку."
            )


def validate_execution_time(execution_time):
    if execution_time > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")


def validate_periodicity(periodicity):
    if periodicity > 7:
        raise ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")
