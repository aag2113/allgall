from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    product_key = models.CharField(max_length=20, unique=True)
    is_real = models.BooleanField(default=False)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.product_key


class Article(models.Model):
    products = models.ManyToManyField(Product)

    uri = models.TextField(null=True, blank=True)
    docid = models.IntegerField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=250)
    word_count = models.IntegerField(null=True, blank=True)
    is_known = models.BooleanField(default=False)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.uri

    @property
    def product(self):
        return self.products.all()[0].product_key


class FcUser(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.username:
            return self.username
        else:
            return str(self.id)
