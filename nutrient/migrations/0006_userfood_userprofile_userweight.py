# Generated by Django 5.1 on 2024-08-10 21:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nutrient", "0005_alter_imageresponsecache_response"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserFood",
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
                ("serving", models.FloatField(default=1)),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("B", "Breakfast"),
                            ("L", "Lunch"),
                            ("D", "Dinner"),
                            ("S", "Snack"),
                        ],
                        max_length=1,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nutrient.nutrient",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="consumed_foods",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("nickname", models.CharField(max_length=50)),
                ("age", models.PositiveSmallIntegerField()),
                ("height", models.PositiveSmallIntegerField()),
                ("weight", models.PositiveSmallIntegerField()),
                (
                    "activity_level",
                    models.CharField(
                        choices=[("L", "Low"), ("M", "Medium"), ("H", "High")],
                        max_length=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("due_date", models.DateField(null=True)),
                ("birth_count", models.PositiveSmallIntegerField(null=True)),
                ("gestational_diabetes", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserWeight",
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
                ("weight", models.FloatField()),
                ("created_at", models.DateField(auto_now_add=True, unique=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="weights",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
