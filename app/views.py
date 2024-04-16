from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from datetime import datetime
from django.http import HttpRequest
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, PasswordChangingForm, ProductForm
from django.contrib.auth.decorators import login_required
#--
import smtplib
import ssl
import certifi
from email.message import EmailMessage
import imghdr

def send_product_email(product, request):#
    email_receiver = request.user.email
    subject = "Your Product was added succesfully"
    body = f"""
        Hello {request.user.username},

        The product "{product.name}" was added succesfully to the category "{product.get_category_display()}". 
        """

    send_email(product, email_receiver, subject, body)
#

def contact_seller(request, product_id):
    product = Product.objects.get(id=product_id)

    subject = f"I would like to buy yout product {product.name}"
    body =  f"""Hello, my name is {request.user.username}.
        I saw at GreenThread the product {product.name} that you are selling.
        I would like to buy it,
        if said product is still avilable, please contact me at {request.user.email}"""

    send_email(product, product.user.email, subject, body)
    return home_page(request) # stay on same page


def send_email(product, email_receiver, subject, body):#
    email_sender = "greenthread69@gmail.com"
    email_password = 'fdkz qydb otip bpag'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    if product.image:#
        with open(product.image.path, 'rb') as img:#
            img_data = img.read()
            img_type = imghdr.what(None, img_data)
            em.add_attachment(img_data, maintype='image', subtype=img_type,filename=product.image.name)
        #
    #
    context = ssl.create_default_context(cafile=certifi.where())
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:#
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
    #
#

#Add Products
@login_required
def add_product(request):#
    if request.method == 'POST':#
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():#

            product = form.save(commit=False)
            product.user = request.user
            product.save()
            send_product_email(product, request)
            messages.success(request, 'The Product successfully uploaded')
            return redirect('add_product')
        #
    #
    else:#
        form = ProductForm()
    #
    return render(request, 'app/add_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return show_products(request)


#
#My Products
@login_required
def show_products(request):#

    products = Product.objects.filter(user=request.user)
    return render(request, 'app/show_products.html', {'products': products})
#

def home(request):#
    return render(request, 'app/index.html', {'title': 'Home Page', 'year': datetime.now().year})
#
def signup(request):
    """Handles user signup. Upon successful registration, redirects to the home page."""
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

def home_page(request, category_name=None):
    """Renders the home page, showing the welcome message and user authentication options."""
    if not category_name:
        category_name="women"

    
    products = Product.objects.filter(category=category_name)
    return render(request, 'app/HomePage.html', {
        'title': 'Home Page',
        'year': datetime.now().year,
        'products': products

    })

@login_required
def view_profile(request):

    """View function for displaying the user profile page."""
    return render(request, 'app/view_profile.html')

def product_category(request, category_name):#
    """Displays products filtered by the given category name."""
    products = Product.objects.filter(category=category_name)
    return render(request, 'app/product_category.html', {'products': products, 'category': category_name})
#


@login_required
def editProfile(request):
    """Allows users to edit their profile and password."""
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangingForm(data=request.POST, user=request.user)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Important for maintaining the session
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('view_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangingForm(user=request.user)
    context = {'user_form': user_form, 'password_form': password_form}
    return render(request, 'app/editProfile.html', context)

