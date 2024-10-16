# Generated by Django 5.0.2 on 2024-09-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ourusers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_student",
            field=models.BooleanField(default=True),
        ),
    ]
