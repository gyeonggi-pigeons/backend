# Generated by Django 5.1 on 2024-08-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nutrient", "0002_alter_nutrient_food_weight_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoResponseCache",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo_hash", models.CharField(max_length=255)),
                ("response", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
