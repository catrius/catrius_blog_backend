import pytest
from django.test import TestCase

from blog.factories.category_factory import CategoryFactory
from blog.models import Category, category
from blog.tests.mixins import FixtureMixin


class CategoryTestCase(TestCase, FixtureMixin):
    def test_str(self):
        life_style_category = CategoryFactory(name='Life Style')
        assert str(life_style_category) == 'Life Style'

    @pytest.mark.django_db
    def test_save(self):
        unique_slugify = self.mocker.spy(category, 'unique_slugify')
        life_style_category = CategoryFactory(name='Life Style')
        unique_slugify.assert_called_once_with(Category, 'Life Style')
        self.mocker.resetall()

        life_style_category.name = 'Vietnamese Life Style'
        life_style_category.save()
        unique_slugify.assert_not_called()
