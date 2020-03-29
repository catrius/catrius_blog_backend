from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from blog.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

    post_count = IntegerField(source='posts.count')
