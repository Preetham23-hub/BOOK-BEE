from django import forms
from .models import Pdf

class BookForm(forms.ModelForm):
    class Meta:
        model=Pdf
        fields=('title','author','image','pdf')
        exclude=['sname']

