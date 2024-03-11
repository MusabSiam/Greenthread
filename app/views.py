"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import SignUpForm
from django.http import HttpRequest
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import ClothingItem
from django.contrib.auth import get_user_model

User = get_user_model()


# Now we can use User.objects.create_user() or other queryset methods.


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/HomePage.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # save() returns the User model instance if 'commit=True' which is default
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')  # Explicitly specifying the backend
            return redirect('home')  # Redirect to the home page or any other appropriate page
        else:
            # You can pass form.errors to the template if you want to display them
            return render(request, 'app/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})


# ---
def home_page(request):
    """Renders the home page."""
    return render(request, 'app/HomePage.html', {
        'title': 'Home Page',
        'year': datetime.now().year,
    })


def category_items(request, category_id):
    items = ClothingItem.objects.filter(category=category_id)
    return render(request, 'app/category_items.html', {'items': items})


def about(request):
    return render(request, 'app/about.html', {'title': 'About'})


def index(request):
    return render(request, 'app/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Example: printing to console (for debugging purposes or replace with email sending logic)
            print(f"Contact form submitted by {name} with email {email}: {message}")

            # Example: sending an email (make sure you have EMAIL_* settings configured in settings.py)
            send_mail(
                subject=f"Contact Form Submission by {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Redirect after POST
            return redirect('contact_thanks')  # Redirect to a new URL for thanking the user after submission
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})

