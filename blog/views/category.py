from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Category
from blog.serializers.category import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all().prefetch_related('posts')
    serializer_class = CategorySerializer
    lookup_field = 'slug'
