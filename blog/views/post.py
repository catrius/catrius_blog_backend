from rest_framework.viewsets import ReadOnlyModelViewSet
from watson import search as watson

from blog.models import Post
from blog.serializers.post import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        category = self.request.query_params.get('category', None)
        search_query = self.request.query_params.get('q', None)

        if category is not None:
            return queryset.filter(category__pk=category)

        if search_query is not None:
            return watson.filter(Post, search_query)

        return queryset
