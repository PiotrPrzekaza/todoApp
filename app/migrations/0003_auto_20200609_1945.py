# Generated by Django 3.0.7 on 2020-06-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200609_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tytul',
            new_name='tytuł',
        ),
    ]