# Generated by Django 4.1.4 on 2023-01-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default="ddffdffs", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
