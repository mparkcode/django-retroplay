from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2038)]

    credit_card_number = forms.CharField(label='Credit card number', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(label='CVV', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'street_address1': forms.TextInput(attrs={'class': 'form-control'}),
            'street_address2': forms.TextInput(attrs={'class': 'form-control'}),
            'town_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }