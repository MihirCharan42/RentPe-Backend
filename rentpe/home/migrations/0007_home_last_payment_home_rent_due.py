# Generated by Django 4.2.3 on 2023-08-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_remove_home_last_payment_remove_home_rent_due"),
    ]

    operations = [
        migrations.AddField(
            model_name="home",
            name="last_payment",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="home",
            name="rent_due",
            field=models.DateField(null=True),
        ),
    ]
