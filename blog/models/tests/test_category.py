import pytest

from blog.factories.category_factory import CategoryFactory
from blog.models import Category, category


@pytest.mark.django_db
class CategoryTestCase:
    def test_str(self):
        life_style_category = CategoryFactory(name='Life Style')
        assert str(life_style_category) == 'Life Style'

    @pytest.mark.django_db
    def test_save(self, mocker):
        unique_slugify = mocker.spy(category, 'unique_slugify')
        life_style_category = CategoryFactory(name='Life Style')
        unique_slugify.assert_called_once_with(Category, 'Life Style')
        mocker.resetall()

        life_style_category.name = 'Vietnamese Life Style'
        life_style_category.save()
        unique_slugify.assert_not_called()
