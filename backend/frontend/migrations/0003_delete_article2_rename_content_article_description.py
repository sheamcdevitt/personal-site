# Generated by Django 4.1 on 2022-08-15 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_article2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article2',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='description',
        ),
    ]
