from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from blog.models import Category
from blog.serializers.post_serializer import PostSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'post_count']

    post_count = IntegerField(source='posts.count')


class CategoryWithPostsSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'description', 'posts', 'post_count']

    posts = PostSerializer(many=True)
    post_count = IntegerField(source='posts.count')
