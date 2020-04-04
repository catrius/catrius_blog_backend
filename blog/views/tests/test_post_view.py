from django.urls import reverse
from rest_framework.test import APITestCase

from blog.factories.category_factory import CategoryFactory
from blog.factories.post_factory import PostFactory


class PostViewTestCase(APITestCase):
    def setUp(self):
        self.categories = CategoryFactory.create_batch(3)

        self.posts = []
        for category in self.categories:
            self.posts.extend(PostFactory.create_batch(3, category=category))

    def assert_result(self, result, category, post):
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

    def test_get_all_posts(self):
        response_data = self.client.get(reverse('blog:posts-list')).data
        assert response_data['count'] == 9
        assert response_data['page_count'] == 1

        results = response_data['results']

        for index, [result, post] in enumerate(zip(results, self.posts)):
            category = self.categories[int(index/3)]
            self.assert_result(result, category, post)

    def test_get_posts_in_category(self):
        category = self.categories[0]
        path = f"{reverse('blog:posts-list')}?category={category.slug}"
        response_data = self.client.get(path).data
        assert response_data['count'] == 3
        assert response_data['page_count'] == 1

        results = response_data['results']

        for result, post in zip(results, self.posts):
            self.assert_result(result, category, post)


class PostViewSearchTestCase(APITestCase):
    def test_search_posts(self):
        PostFactory(
            title='Corona',
            content='This is one of the worst pandemic in the last 10 years.',
            excerpt='Worst pandemic',
            caption='Corona',
        )
        PostFactory(
            title='Covid 19',
            content='This is the most deadly disease caused by the corona virus in the last 10 years.',
            excerpt='A lot of people have been killed.',
            caption='Covid 19',
        )

        response_data = self.client.get(f"{reverse('blog:posts-list')}?q='Covid 19'").data
        assert response_data['count'] == 1

        response_data = self.client.get(f"{reverse('blog:posts-list')}?q='10 years'").data
        assert response_data['count'] == 2

        response_data = self.client.get(f"{reverse('blog:posts-list')}?q='people'").data
        assert response_data['count'] == 1
