from rest_framework.serializers import ModelSerializer

from blog.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']
