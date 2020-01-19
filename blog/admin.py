from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models.category import Category
from blog.models.post import Post


class PostAdmin(ModelAdmin):
    list_display = ('title', 'category', 'excerpt', 'tags')


class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
