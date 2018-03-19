from django import forms
from .models import Pytanie, Wybor, Grupa, Ankieta



class StworzPytanie(forms.ModelForm):
    class Meta:
        model = Pytanie
        fields = ['pytanie_text', 'pytanie_plik', 'grupa', 'ankieta']
        exclude = ['autor', 'pub_date']




class StworzWybor(forms.ModelForm):
    class Meta:
        model = Wybor
        fields = '__all__'
        exclude = ['votes', 'pytanie']



class StworzAnkiete(forms.ModelForm):
    class Meta:
        model = Ankieta
        fields = ['nazwa_ankiety',]


class StworzGrupe(forms.ModelForm):
    class Meta:
        model = Grupa
        fields = ['nazwa_grupy', 'ankieta',]
