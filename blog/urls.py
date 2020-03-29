from django.urls import include, path
from rest_framework import routers

from blog.views.category_view_set import CategoryViewSet
from blog.views.post_view_set import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, 'posts')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
