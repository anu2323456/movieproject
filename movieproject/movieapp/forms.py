from django import forms
from .models import Movie

class Forms(forms.ModelForm):
    class Meta:
        fields=['name','desc','year','img']
        model=Movie