from rest_framework.viewsets import ReadOnlyModelViewSet

from blog.models import Post
from blog.serializers.post import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
