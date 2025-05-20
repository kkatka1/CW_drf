from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("users:register")
        self.login_url = reverse("users:login")

    def test_user_registration(self):
        data = {
            "email": "user@example.com",
            "password": "pass1234",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="user@example.com").exists())

    def test_user_login(self):
        User.objects.create_user(email="user2@example.com", password="pass1234")
        data = {"email": "user2@example.com", "password": "pass1234"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid_password(self):
        User.objects.create_user(email="user3@example.com", password="pass1234")
        data = {"email": "user3@example.com", "password": "wrongpass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 401)
        self.assertNotIn("access", response.data)
