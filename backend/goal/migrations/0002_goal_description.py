# Generated by Django 3.2 on 2021-05-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
