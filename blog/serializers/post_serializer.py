from rest_framework.serializers import ModelSerializer

from blog.models import Post
from blog.serializers.category_serializer import CategorySerializer
from blog.serializers.serializer_mixins import NoneOmittedSerializerMixin


class PostSerializer(NoneOmittedSerializerMixin, ModelSerializer):
    class Meta:
        model = Post
        exclude = ['id']

    category = CategorySerializer()
