from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Extending Django's AbstractUser to include additional fields
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('volunteer', 'Volunteer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    birth_date = models.DateField(null=True, blank=True)


# Use AUTH_USER_MODEL in ForeignKey and ManyToManyField like so:
from django.conf import settings


class ClothingItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    size = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothes_images/', blank=True, null=True)


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExchangeRequest(models.Model):
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, related_name='requests_made', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='requests_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=50,
                              choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')])


class Review(models.Model):
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
