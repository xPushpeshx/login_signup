# Generated by Django 3.2.9 on 2022-02-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20220201_2146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lforms',
        ),
        migrations.DeleteModel(
            name='Sforms',
        ),
    ]
