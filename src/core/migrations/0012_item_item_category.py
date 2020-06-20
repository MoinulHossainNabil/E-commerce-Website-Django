# Generated by Django 3.0.7 on 2020-06-18 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
            preserve_default=False,
        ),
    ]
