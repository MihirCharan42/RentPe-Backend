# Generated by Django 4.2.3 on 2023-07-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=25)),
                ("email", models.CharField(max_length=25, unique=True)),
                ("mobile", models.CharField(max_length=15, unique=True)),
                ("password", models.CharField(max_length=25)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
