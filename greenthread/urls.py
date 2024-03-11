"""
Definition of urls for greenthread.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import category_items, about
from django.urls import path
from app.views import index  # Make sure to import the index view

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home_page, name='home'),
    path('login/',
         LoginView.as_view(
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={'title': 'Log in', 'year': datetime.now().year},
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('categories/<int:category_id>/', views.category_items, name='category_items'),
    path('about/', views.about, name='about'),  # Ensure you have an 'about' view in your views.py
    path('contact/', views.contact, name='contact'),  # Assuming you will add a 'contact' view
    path('admin/', admin.site.urls),
]
