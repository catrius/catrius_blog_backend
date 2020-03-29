from django.test import TestCase

from blog.factories.category import CategoryFactory


class CategoryTestCase(TestCase):
    def test_str(self):
        category = CategoryFactory(name='Test Category')
        assert str(category) == 'Test Category'
