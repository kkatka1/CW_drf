from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User
from habits.models import Habit
from django.utils import timezone


class HabitTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="habit@example.com", password="123qwe456rty"
        )
        self.client.force_authenticate(user=self.user)
        self.habits_url = reverse("habits:habit-list")

    def test_create_habit(self):
        data = {
            "place": "Кухня",
            "time": timezone.now().strftime("%H:%M:%S"),
            "action": "Помыть посуду",
            "execution_time": 60,
            "periodicity": 1,
            "is_public": True,
            "is_pleasant": False,
        }
        response = self.client.post(self.habits_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.first().action, "Помыть посуду")

    def test_create_invalid_habit_with_reward_and_related(self):
        pleasant = Habit.objects.create(
            user=self.user,
            place="Ванная",
            time=timezone.now(),
            action="Принять ванну",
            is_pleasant=True,
            execution_time=60,
            periodicity=1,
        )

        data = {
            "place": "Балкон",
            "time": timezone.now().strftime("%H:%M:%S"),
            "action": "Почитать",
            "execution_time": 60,
            "periodicity": 1,
            "reward": "Шоколад",
            "related_habit": pleasant.id,
        }
        response = self.client.post(self.habits_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("non_field_errors", response.data or response.data.keys())
