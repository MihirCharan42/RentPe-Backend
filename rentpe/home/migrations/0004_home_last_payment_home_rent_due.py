# Generated by Django 4.2.3 on 2023-08-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_home_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="home",
            name="last_payment",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="home",
            name="rent_due",
            field=models.DateField(default=None),
        ),
    ]
