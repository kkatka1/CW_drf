from rest_framework import serializers
from .models import Habit
from .validators import (
    validate_reward_and_related,
    validate_pleasant_habit,
    validate_execution_time,
    validate_periodicity,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)

    def validate(self, data):
        validate_reward_and_related(data.get("reward"), data.get("related_habit"))

        validate_pleasant_habit(
            data.get("is_pleasant"), data.get("reward"), data.get("related_habit")
        )

        validate_execution_time(data.get("execution_time", 0))
        validate_periodicity(data.get("periodicity", 1))

        return data
