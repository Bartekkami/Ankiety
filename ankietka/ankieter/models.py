from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class Ankieta(models.Model):
    nazwa_ankiety = models.CharField(max_length=30, default=None)
    def __str__(self):
        return self.nazwa_ankiety
    class Meta:
        verbose_name = 'Ankieta'
        verbose_name_plural = 'Ankiety'



class Grupa(models.Model):
    ankieta = models.ForeignKey(Ankieta, on_delete=models.CASCADE, default=None)
    nazwa_grupy = models.CharField(max_length=30, default=None)
    def __str__(self):
        return self.nazwa_grupy
    class Meta:
        verbose_name = 'Grupa'
        verbose_name_plural = 'Grupy'



class Pytanie(models.Model):
    ankieta = models.ForeignKey(Ankieta, on_delete=models.CASCADE, default=None, blank=True)
    grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE, default=None, blank=True)
    pytanie_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    pytanie_plik = models.ImageField(default=None, blank=True, null=True)
    autor = models.ForeignKey(User, default=None, on_delete=None)
    def __str__(self):
        return self.pytanie_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Pytanie'
        verbose_name_plural = 'Pytania'



class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    wybor_text = models.CharField(max_length=200, blank=True)
    votes = models.IntegerField(default=0)
    plik = models.ImageField(default=None, blank=True)
    def __str__(self):
        return self.wybor_text
    class Meta:
        verbose_name = 'Wybor'
        verbose_name_plural = 'Wybory'
