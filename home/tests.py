from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class MessagePageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/questions/")
        self.assertEqual(response.status_code,200)

# Create your tests here.

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home:questions'))
        self.assertEqual(response.status_code,200)
