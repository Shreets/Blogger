# Generated by Django 3.0.8 on 2020-07-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=None, upload_to='blog/images/'),
        ),
    ]