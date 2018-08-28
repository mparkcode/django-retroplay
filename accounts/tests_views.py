from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

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
        
    def test_user_can_log_in(self):
        test_user = User.objects.create_user(username="test", email="test@example.com", password="Madetotest")
        response = self.client.post("/accounts/login", {
            'username': 'test',
            'password': 'Madetotest'
        })
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_error_on_login(self):
        response = self.client.post("/accounts/login", {
            'username': 'test',
            'password': 'Madetotest'
        })
        self.assertFormError(response, 'form', None, "Your username or password are incorrect")
        
    def test_user_can_register(self):
        response = self.client.post("/accounts/register", {
            'username': 'test',
            'email': 'test@email.com',
            'password1': 'Madetotest',
            'password2': 'Madetotest'
        })
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_error_on_registration(self):
        form_params={
            'username': 'test',
            'email': 'test@email.com',
            'password1': 'Madtotest',
            'password2': 'Madetotest'
        }
        response = self.client.post("/accounts/register", form_params)
        form = UserRegistrationForm(form_params)
        self.assertFalse(form.is_valid())