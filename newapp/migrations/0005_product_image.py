# Generated by Django 5.0.4 on 2024-06-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0004_rename_orderitem_orderitems"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]