from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm, SignUpForm
class TestViews(TestCase):  
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.home_page_url = reverse('home_page')
        self.view_profile_url = reverse('view_profile')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_home_page_GET(self):
        response = self.client.get(self.home_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/HomePage.html')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/signup.html')

    def test_signup_POST_valid(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertEqual(User.objects.count(), 2)  # Including the user created in setUp
    def test_signup_POST_invalid(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Wrongpassword'
    })
        self.assertEqual(response.status_code, 200)  # Stay on page due to form error
        self.assertTrue('form' in response.context)  # ודא כי יש טופס ב-context
        form = response.context['form']  # קבל את הטופס מה-context
        self.assertFalse(form.is_valid())  # ודא כי הטופס אינו תקף
        self.assertIn('password2', form.errors)  # ודא כי יש שגיאה בשדה password2


    def test_view_profile_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.view_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/view_profile.html')

    def test_view_profile_unauthenticated(self):
        response = self.client.get(self.view_profile_url)
        self.assertNotEqual(response.status_code, 200)  # Expected redirect or failure due to @login_required"""


class TestProductViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='12345')
        self.client.login(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', category='men', user=self.user, image=None)
        self.add_product_url = reverse('add_product')
        self.show_products_url = reverse('show_products')

    def test_add_product_GET(self):
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/add_product.html')

    #def test_show_products_GET(self):
     ##   response = self.client.get(self.show_products_url)
       # self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'Test Product')

class TestAuthenticationViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.home_page_url = reverse('home_page')
        self.view_profile_url = reverse('view_profile')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_home_page_GET(self):
        response = self.client.get(self.home_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/HomePage.html')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/signup.html')

    def test_signup_POST_valid(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_signup_POST_invalid(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_view_profile_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.view_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/view_profile.html')

    def test_view_profile_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.view_profile_url)
        self.assertNotEqual(response.status_code, 200)
