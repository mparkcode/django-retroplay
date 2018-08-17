from django.test import TestCase
from .forms import GameSearchForm

# Create your tests here.
class TestProductsForms(TestCase):
    
    def test_game_search_form(self):
        form=GameSearchForm({
            'query': 'some game'
        })
        self.assertTrue(form.is_valid())
    
    def test_game_search_form_query_required(self):
        form=GameSearchForm({
            'query': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['query'], ['This field is required.'])   