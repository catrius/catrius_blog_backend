from django.db.models import Model, TextField, CharField, SlugField, BooleanField

from blog.utils import unique_slugify


class Category(Model):
    slug = SlugField(max_length=128)
    name = CharField(max_length=128, unique=True)
    description = TextField()
    is_page = BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(Category, self.name)

        return super(Category, self).save(*args, **kwargs)
