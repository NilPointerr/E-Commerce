# Generated by Django 3.2.12 on 2023-02-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_orders_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
