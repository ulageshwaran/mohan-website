# Generated by Django 5.0.4 on 2024-06-01 06:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0003_orderitem_shippingadress"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderItem",
            new_name="OrderItems",
        ),
    ]