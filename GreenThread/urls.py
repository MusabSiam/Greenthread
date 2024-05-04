"""
URL configuration for GreenThread project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app.views import home,signup,home_page
from django.contrib.auth.views import LoginView
from datetime import datetime
from app import views


from app import forms


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='app/login.html', authentication_form=forms.BootstrapAuthenticationForm, extra_context={'title': 'Log in', 'year': datetime.now().year}), name='login'),
    path('accounts/profile/', views.home_page, name='home_page'),
    #path('accounts/profile/', view_profile, name='profile'),
]

#---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)