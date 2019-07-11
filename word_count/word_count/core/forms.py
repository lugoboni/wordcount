from django import forms

from .models import ()

class WordCountForm(forms.Form):
    
    words = forms.IntegerField(
        label='WORDS TO COUNT',
        widget=forms.TextInput()
    )