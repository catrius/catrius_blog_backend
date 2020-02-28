from collections import OrderedDict

from rest_framework.fields import SkipField


class NoneOmittedSerializerMixin:
    def to_representation(self, instance):
        data = super(NoneOmittedSerializerMixin, self).to_representation(instance)
        return {key: value for key, value in data.items() if value is not None}
