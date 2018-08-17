# products forms

from django import forms


class GameSearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search game shop'}), label="")