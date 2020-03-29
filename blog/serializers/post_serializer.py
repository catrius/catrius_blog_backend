from rest_framework.serializers import ModelSerializer

from blog.models import Post, Category
from blog.serializers.serializer_mixins import NoneOmittedSerializerMixin


class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'name']


class PostSerializer(NoneOmittedSerializerMixin, ModelSerializer):
    class Meta:
        model = Post
        exclude = ['id']

    category = PostCategorySerializer()
