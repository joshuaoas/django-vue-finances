# Generated by Django 3.2 on 2021-05-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='source',
            new_name='title',
        ),
    ]