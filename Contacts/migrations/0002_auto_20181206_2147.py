# Generated by Django 2.1.4 on 2018-12-06 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Person',
        ),
    ]
