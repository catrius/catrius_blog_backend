from django.db.models import Model, TextField, CharField


class Category(Model):
    name = CharField(max_length=128, unique=True)
    description = TextField()

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
