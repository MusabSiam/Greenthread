from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings



urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('show/', views.show_products, name='show_products'),
    path('signup/', views.signup, name='signup'),
    path('home/<str:category_name>/', views.home_page, name='home_page_by_category'),
    path('home/', views.home_page, name='home_page'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('category/<str:category_name>/', views.home_page, name='product_category'),
    #path('login/', LoginView.as_view(template_name='app/login.html', authentication_form=forms.BootstrapAuthenticationForm, extra_context={'title': 'Log in', 'year': datetime.now().year}), name='login'),
    path('contact_seller/<str:product_id>/', views.contact_seller, name='contact_seller'),
    path('delete_product/<str:product_id>/', views.delete_product, name='delete_product'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('viewProfile/', views.view_profile, name='viewProfile'),
    path('editProfile/', views.editProfile, name='editProfile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)