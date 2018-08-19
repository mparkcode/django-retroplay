from django.test import TestCase

# Create your tests here.
class TestAccountsViews(TestCase):
    
    def test_get_login_page(self):
        page = self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/login.html")
        
    def test_get_register_page(self):
        page = self.client.get("/accounts/register")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/register.html")
        
    def test_get_profile_page(self):
        page = self.client.get("/accounts/profile")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "accounts/profile.html")
        
    def test_logout(self):
        response = self.client.get("/accounts/logout")
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    
        