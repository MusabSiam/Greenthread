from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from datetime import datetime


class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'app/index.html')

    def test_home_view_context_data(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['title'], 'Home Page')
        self.assertEqual(response.context['year'], datetime.now().year)


class SignupViewTests(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }

    def test_signup_view_get_request(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/signup.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_signup_view_post_request_with_valid_data_creates_user(self):
        response = self.client.post(reverse('signup'), self.form_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_view_post_request_with_valid_data_redirects_to_home(self):
        response = self.client.post(reverse('signup'), self.form_data)
        self.assertRedirects(response, reverse('home'))

    # Additional tests can include invalid data submissions and form errors


class HomePageViewTests(TestCase):
    def test_home_page_view_status_code(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, 'app/HomePage.html')

    def test_home_page_view_context_data(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.context['title'], 'Home Page')
        self.assertEqual(response.context['year'], datetime.now().year)

# Additional utility tests or setup can go here
