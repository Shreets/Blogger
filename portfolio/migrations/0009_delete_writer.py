# Generated by Django 3.0.8 on 2020-07-17 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_remove_writer_blog_written'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Writer',
        ),
    ]
