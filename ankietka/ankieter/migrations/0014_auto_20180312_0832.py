# Generated by Django 2.0.2 on 2018-03-12 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieter', '0013_pytanie_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytanie',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
