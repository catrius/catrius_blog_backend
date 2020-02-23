from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models.category import Category
from blog.models.post import Post


class PostAdmin(ModelAdmin):
    list_display = ['title', 'category', 'excerpt', 'tags']
    list_select_related = ['category']
    exclude = ['created', 'modified']


class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'description']
    exclude = ['created', 'modified']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
