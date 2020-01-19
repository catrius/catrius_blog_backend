from django.urls import include, path
from rest_framework import routers

from blog.views.category_view import CategoryViewSet
from blog.views.post_view import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
