# Generated by Django 5.0.3 on 2024-04-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.FileField(blank=True, upload_to="project_images/"),
        ),
    ]
