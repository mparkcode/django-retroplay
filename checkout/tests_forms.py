from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

# Create your tests here.
class TestCheckoutForms(TestCase):
    
    def test_make_payment_form(self):
        form=MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '111',
            'expiry_month': 10,
            'expiry_year': 2019,
            'stripe_id': 'something'
        })
        self.assertTrue(form.is_valid())
        
    
    def test_order_form(self):
        form=OrderForm({
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'street_address1': '10 fake street',
            'street_address2': 'apartment 10',
            'town_or_city': 'Some City',
            'county': 'Some County',
            'country': 'Some Country',
            'postcode': 'A12D34'
        })
        self.assertTrue(form.is_valid())
        
    def test_order_street_address_2_not_required(self):
            form=OrderForm({
                'full_name': 'John Doe',
                'phone_number': '123456789',
                'street_address1': '10 fake street',
                'town_or_city': 'Some City',
                'county': 'Some County',
                'country': 'Some Country',
                'postcode': 'A12D34'
            })
            self.assertTrue(form.is_valid())
            
    def test_order_street_postcode_not_required(self):
            form=OrderForm({
                'full_name': 'John Doe',
                'phone_number': '123456789',
                'street_address1': '10 fake street',
                'town_or_city': 'Some City',
                'county': 'Some County',
                'country': 'Some Country',
            })
            self.assertTrue(form.is_valid())
        
    def test_order_form_full_name_required(self):
        form=OrderForm({
            'phone_number': '123456789',
            'street_address1': '10 fake street',
            'street_address2': 'apartment 10',
            'town_or_city': 'Some City',
            'county': 'Some County',
            'country': 'Some Country',
            'postcode': 'A12D34'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], ['This field is required.'])
        
    def test_order_form_street_address1_required(self):
        form=OrderForm({
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'street_address2': 'apartment 10',
            'town_or_city': 'Some City',
            'county': 'Some County',
            'country': 'Some Country',
            'postcode': 'A12D34'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['street_address1'], ['This field is required.'])
        
    def test_order_form_town_or_city_required(self):
        form=OrderForm({
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'street_address1': '10 fake street',
            'street_address2': 'apartment 10',
            'county': 'Some County',
            'country': 'Some Country',
            'postcode': 'A12D34'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['town_or_city'], ['This field is required.'])
        
    def test_order_form_county_required(self):
        form=OrderForm({
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'street_address1': '10 fake street',
            'street_address2': 'apartment 10',
            'town_or_city': 'Some City',
            'country': 'Some Country',
            'postcode': 'A12D34'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['county'], ['This field is required.'])
        
    def test_order_form_country_required(self):
        form=OrderForm({
            'full_name': 'John Doe',
            'phone_number': '123456789',
            'street_address1': '10 fake street',
            'street_address2': 'apartment 10',
            'town_or_city': 'Some City',
            'county': 'Some county',
            'postcode': 'A12D34'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['country'], ['This field is required.'])
        