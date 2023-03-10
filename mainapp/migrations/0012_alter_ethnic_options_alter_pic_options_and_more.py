# Generated by Django 4.1.3 on 2023-01-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0011_alter_ethnic_options_alter_pic_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ethnic",
            options={},
        ),
        migrations.AlterModelOptions(
            name="pic",
            options={},
        ),
        migrations.AlterModelOptions(
            name="tourism",
            options={},
        ),
        migrations.AddField(
            model_name="tourism",
            name="img_index",
            field=models.ImageField(default=0, upload_to="tourism"),
            preserve_default=False,
        ),
    ]
