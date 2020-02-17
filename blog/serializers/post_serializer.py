from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'category', 'content', 'excerpt', 'tags', 'created', 'modified']

    category = SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
