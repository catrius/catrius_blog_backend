from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Post
from blog.serializers.post import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.request.query_params.get('category', None)
        if category is None:
            return queryset
        return queryset.filter(category__pk=category)
