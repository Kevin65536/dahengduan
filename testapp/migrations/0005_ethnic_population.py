# Generated by Django 4.1.3 on 2023-01-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0004_ethnic"),
    ]

    operations = [
        migrations.AddField(
            model_name="ethnic",
            name="population",
            field=models.CharField(default=100, max_length=20),
            preserve_default=False,
        ),
    ]
