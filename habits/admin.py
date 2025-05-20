from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """
    Админка модели Habit
    """

    list_display = (
        "id",
        "user",
        "action",
        "time",
        "is_pleasant",
        "related_habit",
        "reward",
        "periodicity",
        "execution_time",
        "is_public",
    )
    list_filter = ("is_pleasant", "is_public")
    search_fields = ("action", "place")
