from rest_framework.serializers import ModelSerializer

from blog.models import Post, Category


class PostCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'category', 'content', 'excerpt', 'tags', 'created', 'modified']

    category = PostCategorySerializer()
