from django import forms
from .models import Pytanie, Wybor



class StworzAnkiete(forms.ModelForm):
    class Meta:
        model = Pytanie
        fields = ['pytanie_text', 'pytanie_plik']
        exclude = ['autor', 'pub_date']



class StworzWybor(forms.ModelForm):
    class Meta:
        model = Wybor
        fields = '__all__'
        exclude = ['votes', 'pytanie']
