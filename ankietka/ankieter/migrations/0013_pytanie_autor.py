# Generated by Django 2.0.2 on 2018-03-11 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ankieter', '0012_remove_pytanie_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytanie',
            name='autor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
