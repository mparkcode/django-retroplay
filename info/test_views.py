from django.test import TestCase
from .forms import QuestionForm

class TestInfoViews(TestCase):
    
    def test_get_contact_page(self):
        page = self.client.get("/info/contact")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "info/contact.html")
        
    def test_search_query_redirect_on_contact(self):
        response = self.client.get("/info/contact?query=test")
        self.assertRedirects(response, '/games/search_results/test', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_get_shipping_page(self):
        page = self.client.get("/info/shipping")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "info/shipping.html")
        
    def test_search_query_redirect_on_shipping(self):
        response = self.client.get("/info/shipping?query=test")
        self.assertRedirects(response, '/games/search_results/test', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_get_faq_page(self):
        page = self.client.get("/info/faq")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "info/faq.html")
        
    def test_search_query_redirect_on_faq(self):
        response = self.client.get("/info/faq?query=test")
        self.assertRedirects(response, '/games/search_results/test', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)