from rest_framework.serializers import ModelSerializer

from blog.models import Post, Category
from blog.serializers.common import NoneOmittedSerializerMixin


class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class PostSerializer(NoneOmittedSerializerMixin, ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk', 'title', 'category', 'content', 'excerpt', 'thumbnail', 'caption', 'image_showing', 'created',
            'modified',
        ]

    category = PostCategorySerializer()
