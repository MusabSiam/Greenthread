from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User  # Correctly import the User model
from .models import Product
from django.utils.translation import gettext_lazy as _
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form that utilizes Bootstrap CSS for styling."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    """Form for user signup, extending Django's UserCreationForm."""
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class UserUpdateForm(UserChangeForm):
    """Form for updating user information."""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')

class PasswordChangingForm(PasswordChangeForm):
    """Form for changing password."""
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')




#Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'category']
