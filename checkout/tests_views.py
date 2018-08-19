from django.test import TestCase

# Create your tests here.
class TestCheckoutViews(TestCase):
    
    def test_checkout_redirects_to_index_if_empty_cart(self):
        response = self.client.get("/checkout/")
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_checkout_confirmation_redirects_to_index_if_empty_cart(self):
        response = self.client.get("/checkout/confirmation")
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)