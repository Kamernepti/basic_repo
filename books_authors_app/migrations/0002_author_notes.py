# Generated by Django 3.1.3 on 2020-11-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
