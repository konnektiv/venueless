# Generated by Django 3.0.6 on 2020-07-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_auto_20200711_1942"),
    ]

    operations = [
        migrations.AddField(
            model_name="membership",
            name="hidden",
            field=models.BooleanField(default=False),
        ),
    ]