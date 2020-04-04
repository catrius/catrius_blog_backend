from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Category
from blog.serializers.category_serializer import CategorySerializer


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
