# Generated by Django 3.0.8 on 2020-07-17 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200717_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
