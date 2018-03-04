from django.contrib import admin

from .models import Product, Article, FcUser

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_key', 'name', 'is_real']
    list_filter = ['is_real']

admin.site.register(Product, ProductAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'docid', 'title', 'word_count', 'is_known']
    list_filter = ['is_known']
    search_fields = ['id', 'docid', 'title']

admin.site.register(Article, ArticleAdmin)


class FcUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    search_fields = ['username']
admin.site.register(FcUser)
