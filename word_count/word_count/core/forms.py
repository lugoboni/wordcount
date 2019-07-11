from django import forms

# from .models import (WordCount)

class WordCountForm(forms.Form):
    
    words = forms.CharField(
        label='WORDS TO COUNT',
        widget=forms.Textarea
    )