from django import forms

class QuestionForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}), label="")
    question = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "10", 'placeholder': 'Enter your message', 'style':'resize:none;' }), label="")