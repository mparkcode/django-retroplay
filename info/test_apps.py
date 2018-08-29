from django.apps import apps
from django.test import TestCase
from .apps import InfoConfig


class TestInfoConfig(TestCase):

    def test_account_app(self):
        self.assertEqual("info", InfoConfig.name)
        self.assertEqual("info", apps.get_app_config("info").name)