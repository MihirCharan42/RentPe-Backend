# Generated by Django 4.2.3 on 2023-08-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_home_last_payment_home_rent_due"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="last_payment",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="home",
            name="rent_due",
            field=models.DateField(blank=True),
        ),
    ]