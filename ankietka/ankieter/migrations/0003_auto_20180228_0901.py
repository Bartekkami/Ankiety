# Generated by Django 2.0.2 on 2018-02-28 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ankieter', '0002_srodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='srodel',
            name='pytanie',
        ),
        migrations.DeleteModel(
            name='Srodel',
        ),
    ]