# Generated by Django 5.0.2 on 2024-02-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("day5app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="std_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
