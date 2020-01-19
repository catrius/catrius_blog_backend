from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, TextField, ForeignKey, CASCADE, CharField, DateTimeField
from django.utils import timezone


class Post(Model):
    title = CharField(max_length=512)
    category = ForeignKey('blog.category', CASCADE, related_name='posts')
    content = TextField()
    excerpt = CharField(max_length=1024)
    tags = ArrayField(CharField(max_length=60))
    created = DateTimeField()
    modified = DateTimeField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)
