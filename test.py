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
