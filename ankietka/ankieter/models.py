from django.db import models
import datetime
from django.utils import timezone


class Pytanie(models.Model):
    pytanie_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.pytanie_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Pytanie'
        verbose_name_plural = 'Pytania'



class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    wybor_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.wybor_text
