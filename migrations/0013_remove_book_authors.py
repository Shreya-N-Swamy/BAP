# Generated by Django 2.1.5 on 2019-02-10 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BAP', '0012_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
    ]
