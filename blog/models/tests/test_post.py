from datetime import datetime

import pytest
from pytz import UTC

from blog.factories.post_factory import PostFactory
from blog.models import post, Post


@pytest.mark.django_db
class PostTestCase:
    def test_str(self):
        corona_post = PostFactory(title='Corona social distance story')
        assert str(corona_post) == 'Corona social distance story'

    @pytest.mark.django_db
    def test_save(self, mocker, freezer):
        unique_slugify = mocker.spy(post, 'unique_slugify')
        freezer.move_to('2020-03-30 03:00')
        corona_post = PostFactory(title='Corona social distance story')

        unique_slugify.assert_called_once_with(Post, 'Corona social distance story')
        assert corona_post.created == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        assert corona_post.modified == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        mocker.resetall()

        freezer.move_to('2020-04-01 08:00')
        corona_post.title = 'Corona social distance story (updated)'
        corona_post.save()
        unique_slugify.assert_not_called()
        assert corona_post.created == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        assert corona_post.modified == datetime(2020, 4, 1, 8, 0, tzinfo=UTC)
