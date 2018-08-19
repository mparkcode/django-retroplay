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