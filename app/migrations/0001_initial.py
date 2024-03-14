# Generated by Django 5.0.3 on 2024-03-14 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("birthdate", models.DateField()),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("email", models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Lawyer",
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
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("birthdate", models.DateField()),
                ("experience", models.IntegerField()),
                ("successful_cases", models.IntegerField()),
                ("unsuccessful_cases", models.IntegerField()),
                ("price", models.PositiveIntegerField()),
                ("characterization", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CaseForm",
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
                ("description", models.TextField()),
                ("article", models.CharField(max_length=255)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="case_forms",
                        to="app.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Case",
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
                ("is_active", models.BooleanField(default=True)),
                ("case_closed_successfully", models.BooleanField()),
                ("article", models.CharField(max_length=255)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_lawyer",
                        to="app.client",
                    ),
                ),
                (
                    "lawyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lawyer_cases",
                        to="app.lawyer",
                    ),
                ),
            ],
        ),
    ]