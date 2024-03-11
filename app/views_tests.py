from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from app.forms import SignUpForm, ContactForm
from datetime import datetime

User = get_user_model()  # Get the custom user model


class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'app/index.html')

    def test_home_view_context_data(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['title'], 'Home')
        self.assertEqual(response.context['year'], datetime.now().year)
