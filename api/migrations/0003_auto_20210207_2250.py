# Generated by Django 3.0.8 on 2021-02-07 17:50

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=api.models.upload_path),
        ),
    ]
