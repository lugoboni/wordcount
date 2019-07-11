from django import forms


class WordCountForm(forms.Form):
    
    words = forms.CharField(
        label='WORDS TO COUNT',
        widget=forms.Textarea
    )