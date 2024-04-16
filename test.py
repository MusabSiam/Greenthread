from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm, SignUpForm
class TestAuthenticationViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.home_page_url = reverse('home_page')
        self.view_profile_url = reverse('view_profile')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_view_profile_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.view_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/view_profile.html')

    def test_view_profile_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.view_profile_url)
        self.assertNotEqual(response.status_code, 200)

