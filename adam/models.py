from django.db import models

# Create your models here.
class BlogPost(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(null=True, blank=True)

    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.CharField(max_length=100)
    author_user = models.CharField(max_length=100, null=True, blank=True)
