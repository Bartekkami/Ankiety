from django import forms
from .models import Pytanie, Wybor



class StworzAnkiete(forms.ModelForm):
    class Meta:
        model = Pytanie
        fields = '__all__'
        exclude = ['autor', 'pub_date']
