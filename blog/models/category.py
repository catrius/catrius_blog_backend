from django.db.models import Model, TextField, CharField


class Category(Model):
    name = CharField(max_length=128)
    description = TextField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
