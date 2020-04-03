from django.urls import reverse
from rest_framework.test import APITestCase

from blog.factories.category_factory import CategoryFactory
from blog.factories.post_factory import PostFactory


class PostViewTestCase(APITestCase):
    @classmethod
    def setup_class(cls):
        cls.categories = CategoryFactory.create_batch(3)

        cls.posts = []
        for category in cls.categories:
            cls.posts.extend(PostFactory.create_batch(3, category=category))

    def test_get_list(self):
        response_data = self.client.get(reverse('blog:posts-list')).data
        assert response_data['count'] == 9
        assert response_data['page_count'] == 1

        results = response_data['results']

        for index, [result, post] in enumerate(zip(results, self.posts)):
            category = self.categories[int(index/3)]

            assert result == {
                'slug': post.slug,
                'title': post.title,
                'content': post.content,
                'excerpt': post.excerpt,
                'thumbnail': f'http://testserver{post.thumbnail.url}',
                'caption': post.caption,
                'image_showing': post.image_showing,
                'created': post.created.isoformat().replace('+00:00', 'Z'),
                'modified': post.modified.isoformat().replace('+00:00', 'Z'),
                'category': {
                    'slug': category.slug,
                    'name': category.name,
                },
            }
