# Generated by Django 2.0.2 on 2018-03-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieter', '0008_auto_20180306_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytanie',
            name='pytanie_plik',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]