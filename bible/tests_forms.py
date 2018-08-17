from django.test import TestCase
from .forms import IgdbSearchForm

# Create your tests here.
class TestBibleForms(TestCase):
    
    def test_igdb_search_form(self):
        form=IgdbSearchForm({
            'igdb_search': 'some game'
        })
        self.assertTrue(form.is_valid())
        
    def test_igdb_search_form_igdb_search_required(self):
        form=IgdbSearchForm({
            'igdb_search': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['igdb_search'], ['This field is required.'])
        
        