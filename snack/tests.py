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

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "cheese")
        self.assertEqual(f"{self.snack.purchaser}", "admin1")
        self.assertEqual(f"{self.snack.description}", "good")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cheese")
        self.assertTemplateUsed(response, "snacks/snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: admin1")
        self.assertTemplateUsed(response, "snacks/snack_detail.html")

    