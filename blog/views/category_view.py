from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Category
from blog.serializers.category_serializer import CategorySerializer


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_page=False).order_by('id')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
