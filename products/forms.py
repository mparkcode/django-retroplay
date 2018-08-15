# products forms

from django import forms


class GameSearchForm(forms.Form):
    query = forms.CharField(label='Search Games Shop', max_length=100)