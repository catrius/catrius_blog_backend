from rest_framework.viewsets import ModelViewSet

from blog.models import Category
from blog.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
