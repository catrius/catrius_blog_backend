from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, TextField, ForeignKey, CASCADE, CharField


class Post(Model):
    title = CharField(max_length=512)
    category = ForeignKey('blog.category', CASCADE, related_name='posts')
    content = TextField()
    excerpt = CharField(max_length=1024)
    tag = ArrayField(CharField(max_length=60))

    def __str__(self):
        return self.title
