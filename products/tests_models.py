from django.test import TestCase
from .models import Brand, Console, Game
# Create your tests here.

class TestProductModel(TestCase):
    
    def test_Brand_Model(self):
        brand=Brand(name="Sony")
        brand.save()
        self.assertEqual(brand.name, "Sony")
        
    def test_Console_Model(self):
        brand=Brand(name="Sony")
        brand.save()
        console = Console(console_type="playstation", brand=brand)
        console.save()
        self.assertEqual(console.console_type, "playstation")    
        self.assertEqual(console.brand, brand)
        
    def test_Game_Model(self):
        brand=Brand(name="Sony")
        brand.save()
        console = Console(console_type="playstation", brand=brand)
        console.save()
        game = Game(title="Example Game", price=4.00, brand=brand, console=console)
        game.save()
        self.assertEqual(game.title, "Example Game")    
        self.assertEqual(game.price, 4.00)
        self.assertEqual(game.brand, brand)
        self.assertEqual(game.console, console)
        
    def test_game_item_as_string(self):
        game = Game(title="Example Game")
        self.assertEqual("Example Game", str(game))
    
        
        
    