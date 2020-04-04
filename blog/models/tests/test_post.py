from datetime import datetime

from django.test import TestCase
from pytz import UTC

from blog.factories.post_factory import PostFactory
from blog.models import post, Post
from blog.tests.mixins import FixtureMixin


class PostTestCase(TestCase, FixtureMixin):
    def test_str(self):
        corona_post = PostFactory(title='Corona social distance story')
        assert str(corona_post) == 'Corona social distance story'

    def test_save(self):
        unique_slugify = self.mocker.spy(post, 'unique_slugify')
        self.freezer.move_to('2020-03-30 03:00')
        corona_post = PostFactory(title='Corona social distance story')

        unique_slugify.assert_called_once_with(Post, 'Corona social distance story')
        assert corona_post.created == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        assert corona_post.modified == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        self.mocker.resetall()

        self.freezer.move_to('2020-04-01 08:00')
        corona_post.title = 'Corona social distance story (updated)'
        corona_post.save()
        unique_slugify.assert_not_called()
        assert corona_post.created == datetime(2020, 3, 30, 3, 0, tzinfo=UTC)
        assert corona_post.modified == datetime(2020, 4, 1, 8, 0, tzinfo=UTC)
