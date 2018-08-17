from django.test import TestCase
from .forms import CommentForm


# Create your tests here.
class TestNewsForms(TestCase):
    
    def test_comment_form(self):
        form=CommentForm({
            'content': 'A comment',
        })
        self.assertTrue(form.is_valid())
        
    def test_comment_form_content_required(self):
        form=CommentForm({
            'content': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['This field is required.'])
        