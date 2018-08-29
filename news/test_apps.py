from django.apps import apps
from django.test import TestCase
from .apps import NewsConfig


class TestNewsConfig(TestCase):

    def test_account_app(self):
        self.assertEqual("news", NewsConfig.name)
        self.assertEqual("news", apps.get_app_config("news").name)