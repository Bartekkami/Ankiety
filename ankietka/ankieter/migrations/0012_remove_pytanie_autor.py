# Generated by Django 2.0.2 on 2018-03-11 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ankieter', '0011_auto_20180311_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pytanie',
            name='autor',
        ),
    ]
