from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Brand, Console, Game
from django.utils import timezone

# Create your tests here.
class TestCheckoutModels(TestCase):
    
    def test_Order_Model(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        self.assertEqual(order.full_name, "John Doe")
        self.assertEqual(order.phone_number, 123456789)
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.postcode, "A12S34")
        self.assertEqual(order.town_or_city, "Some town")
        self.assertEqual(order.street_address1, "1 street_address")
        self.assertEqual(order.street_address2, "2 street address")
        self.assertEqual(order.county, "some county")
        
    def test_order_model_as_string(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        self.assertEqual(str(order.id)+"-"+str(order.date)+"-John Doe", str(order))
        
    
    def test_order_line_item_model(self):
        current_date=timezone.now()
        order = Order(full_name="John Doe", phone_number=123456789, country="Ireland", postcode="A12S34", town_or_city="Some town", street_address1="1 street_address", street_address2="2 street address", county="some county", date=current_date)
        order.save()
        brand=Brand(name="Sony")
        brand.save()
        console = Console(console_type="playstation", brand=brand)
        console.save()
        game = Game(title="Example Game", price=4.00, brand=brand, console=console)
        game.save()
        orderlineitem = OrderLineItem(order=order,game=game,quantity=1)
        orderlineitem.save()
        self.assertEqual(orderlineitem.order, order)
        self.assertEqual(orderlineitem.game, game)
        self.assertEqual(orderlineitem.quantity, 1)
        self.assertEqual("1 Example Game @ 4.0", str(orderlineitem))
        