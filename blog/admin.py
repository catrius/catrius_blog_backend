from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import CharField, TextField
from django.forms import TextInput, Textarea

from blog.models.category import Category
from blog.models.post import Post


class PostAdmin(ModelAdmin):
    list_display = ['title', 'category', 'excerpt']
    list_select_related = ['category']
    exclude = ['created', 'modified']
    readonly_fields = ['slug']

    formfield_overrides = {
        CharField: {'widget': TextInput(attrs={'size': 150})},
        TextField: {'widget': Textarea(attrs={'rows': 30, 'cols': 150})},
    }


class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'description']
    exclude = ['created', 'modified']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
