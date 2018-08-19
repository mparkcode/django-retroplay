from django.test import TestCase
from .models import Brand, Console
# Create your tests here.
class TestProductsViews(TestCase):
    
    def test_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/index.html")
        
    def test_get_all_brands_page(self):
        page = self.client.get("/games/all_brands")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/all_brands.html")
        
    def test_get_show_consoles_page(self):
        brand = Brand(name="Sega")
        brand.save()
        page = self.client.get("/games/{0}".format(brand.name))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/show_consoles.html")
        
    def test_get_show_games_page(self):
        brand = Brand(name="Sega")
        brand.save()
        console = Console(console_type="mega-drive", brand=brand)
        console.save()
        page = self.client.get("/games/show_games/{0}".format(console.console_type))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/show_games.html")
        
    def test_search_query_redirect_on_all_brands(self):
        response = self.client.get("/games/all_brands?query=sonic")
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_show_console(self):
        brand = Brand(name="Sega")
        brand.save()
        response = self.client.get("/games/{0}?query=sonic".format(brand.name))
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_show_games(self):
        brand = Brand(name="Sega")
        brand.save()
        console = Console(console_type="mega-drive", brand=brand)
        console.save()
        response = self.client.get("/games/show_games/{0}?query=sonic".format(console.console_type))
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_search_query_redirect_on_search_results(self):
        response = self.client.get("/games/search_results/sonic?query=sonic")
        self.assertRedirects(response, '/games/search_results/sonic', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)