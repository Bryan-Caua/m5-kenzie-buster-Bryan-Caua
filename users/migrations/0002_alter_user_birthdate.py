# Generated by Django 4.1.7 on 2023-02-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(default=None, null=True),
        ),
    ]