# Generated by Django 4.2.3 on 2023-07-29 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0002_home_landlord_user_home_tenant_user"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "home",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.home",
                    ),
                ),
                (
                    "landlord_user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="landlord_user_transation",
                        to="authentication.user",
                    ),
                ),
                (
                    "tenant_user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tenant_user_transaction",
                        to="authentication.user",
                    ),
                ),
            ],
            options={
                "db_table": "transactions",
            },
        ),
    ]
