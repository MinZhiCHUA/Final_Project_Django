# Generated by Django 4.1 on 2023-04-26 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_product_feedback"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="pred_date",
        ),
        migrations.RemoveField(
            model_name="product",
            name="pred_label_code",
        ),
        migrations.RemoveField(
            model_name="product",
            name="pred_label_text",
        ),
    ]
