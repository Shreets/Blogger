# Generated by Django 3.0.8 on 2020-07-17 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200717_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writer',
            old_name='writer',
            new_name='author',
        ),
    ]
