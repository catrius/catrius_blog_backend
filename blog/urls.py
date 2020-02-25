from django.urls import include, path
from rest_framework import routers

from blog.views.category import CategoryViewSet
from blog.views.post import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
