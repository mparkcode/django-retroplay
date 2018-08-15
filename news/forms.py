# news forms

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
            }
        labels = {
            "content": "Leave a comment"
        }