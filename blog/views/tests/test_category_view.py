from django.urls import reverse
from rest_framework.test import APITestCase

from blog.factories.category_factory import CategoryFactory


class CategoryViewTestCase(APITestCase):
    def test_get_list(self):
        categories = CategoryFactory.create_batch(3)

        response_data = self.client.get(reverse('blog:categories-list')).data
        assert response_data['count'] == 3
        assert response_data['page_count'] == 1
        for result, category in zip(response_data['results'], categories):
            assert result == {
                'name': category.name,
                'slug': category.slug,
                'description': category.description,
            }
