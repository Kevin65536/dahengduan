# Generated by Django 4.1.3 on 2023-01-30 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0007_delete_job_detail"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tourism",
            options={"ordering": ["-longitude"]},
        ),
    ]
