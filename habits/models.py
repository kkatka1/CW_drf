from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits"
    )
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)

    is_pleasant = models.BooleanField(default=False)

    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"is_pleasant": True},
        related_name="related_to",
    )

    reward = models.CharField(max_length=255, blank=True, null=True)
    periodicity = models.PositiveSmallIntegerField(default=1)
    execution_time = models.PositiveSmallIntegerField(help_text="Время в секундах")
    is_public = models.BooleanField(default=False)

    def clean(self):
        if self.related_habit and self.reward:
            raise ValidationError(
                "ННельзя указать и связанную приятную привычку, и награду одновременно."
            )

        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не может иметь награду или связанную привычку."
            )

        if self.execution_time > 120:
            raise ValidationError("Время выполнения не должно превышать 120 секунд.")

        if self.periodicity > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")

        def __str__(self):
            return f"{self.action} в {self.time} - {self.place}"
