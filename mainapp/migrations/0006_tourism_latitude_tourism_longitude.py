# Generated by Django 4.1.3 on 2023-01-11 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_ethnic_population"),
    ]

    operations = [
        migrations.AddField(
            model_name="tourism",
            name="latitude",
            field=models.FloatField(default=118),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tourism",
            name="longitude",
            field=models.FloatField(default=32),
            preserve_default=False,
        ),
    ]