from django.apps import apps
from django.test import TestCase
from .apps import BibleConfig


class TestBibleConfig(TestCase):

    def test_account_app(self):
        self.assertEqual("bible", BibleConfig.name)
        self.assertEqual("bible", apps.get_app_config("bible").name)