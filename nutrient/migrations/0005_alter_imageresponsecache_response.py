# Generated by Django 5.1 on 2024-08-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nutrient", "0004_rename_photoresponsecache_imageresponsecache"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imageresponsecache",
            name="response",
            field=models.JSONField(null=True),
        ),
    ]
