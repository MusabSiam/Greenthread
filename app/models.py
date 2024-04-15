from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):#
    CATEGORY_CHOICES = [
        ('women', 'Women'),
        ('men', 'Men'),
        ('kids', 'Kids'),
        ('over_size', 'Over Size'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):#
        return self.name
    #
#