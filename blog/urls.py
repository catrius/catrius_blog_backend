from django.urls import include, path
from rest_framework import routers

from blog.views.category_view import CategoryView
from blog.views.post_view import PostView

router = routers.DefaultRouter()
router.register(r'posts', PostView, 'posts')
router.register(r'categories', CategoryView, 'categories')

urlpatterns = [
    path('', include(router.urls)),
]
