from django import forms

class IgdbSearchForm(forms.Form):
    igdb_search =   forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search the bible'}))