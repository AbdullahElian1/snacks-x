from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class ThingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin1", email="admin1@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="cheese", description="good", purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "cheese")

    