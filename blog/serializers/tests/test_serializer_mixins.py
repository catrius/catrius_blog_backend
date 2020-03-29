from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from blog.serializers.serializer_mixins import NoneOmittedSerializerMixin


class TestSerializer(NoneOmittedSerializerMixin, Serializer):
    data_field = CharField()
    empty_field = CharField()


class NoneOmittedSerializerMixinTestCase:
    def test_to_representation(self, mocker):
        test_object = mocker.Mock(**{
            'data_field': 'data',
            'empty_field': None,
        })
        assert TestSerializer(test_object).data == {
            'data_field': 'data'
        }
