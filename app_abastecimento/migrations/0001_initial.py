# Generated by Django 4.2.14 on 2024-07-24 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tanque",
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
                (
                    "tipo_combustivel",
                    models.CharField(
                        choices=[("GASOLINA", "Gasolina"), ("DIESEL", "Óleo Diesel")],
                        max_length=50,
                    ),
                ),
                ("data", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
