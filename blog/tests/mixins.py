import pytest


class FixtureMixin:
    @pytest.fixture(autouse=True)
    def __inject_fixtures(self, mocker, freezer):
        self.mocker = mocker
        self.freezer = freezer
