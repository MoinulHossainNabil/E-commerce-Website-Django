# Generated by Django 3.0.7 on 2020-06-18 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200618_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
    ]
