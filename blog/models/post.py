from django.db.models import Model, TextField, ForeignKey, CASCADE, CharField, DateTimeField, BooleanField, SlugField
from django.utils import timezone
from django_resized import ResizedImageField

from blog.utils import unique_slugify


class Post(Model):
    slug = SlugField(max_length=512)
    title = CharField(max_length=512)
    category = ForeignKey('blog.category', CASCADE, related_name='posts')
    content = TextField(blank=True)
    excerpt = CharField(max_length=1024)
    thumbnail = ResizedImageField(
        upload_to='photos/%Y/%m/%d',
        size=[960, 540],
        quality=80,
        null=True,
        blank=True
    )
    caption = CharField(max_length=512, blank=True)
    image_showing = BooleanField(default=True)
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

        if not self.slug:
            self.slug = unique_slugify(Post, self.title)

        return super(Post, self).save(*args, **kwargs)
