from django.test import TestCase
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from blog.serializers.serializer_mixins import NoneOmittedSerializerMixin
from blog.tests.mixins import FixtureMixin


class TestSerializer(NoneOmittedSerializerMixin, Serializer):
    data_field = CharField()
    empty_field = CharField()


class NoneOmittedSerializerMixinTestCase(TestCase, FixtureMixin):
    def test_to_representation(self):
        test_object = self.mocker.Mock(**{
            'data_field': 'data',
            'empty_field': None,
        })
        assert TestSerializer(test_object).data == {
            'data_field': 'data'
        }
