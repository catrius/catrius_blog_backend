from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers.post_serializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
