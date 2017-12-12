from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date_created', 'date_modified', 'date_published')
admin.site.register(BlogPost, BlogPostAdmin)
