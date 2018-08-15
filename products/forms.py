from django import forms
from .models import Game

class GameSearchForm(forms.Form):
    query = forms.CharField(label='Search Games Shop', max_length=100)