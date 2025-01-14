# Generated by Django 3.2.3 on 2021-06-01 15:51

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("control", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="data",
            field=models.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="logentry",
            name="object_id",
            field=models.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder
            ),
        ),
    ]
