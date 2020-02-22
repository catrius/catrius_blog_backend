from django.db.models import Count
from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Category
from blog.serializers.category_serializer import CategorySerializer, CategoryWithPostsSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all().prefetch_related('posts')

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        if self.action == 'retrieve':
            return CategoryWithPostsSerializer
