# Generated by Django 5.0.2 on 2024-09-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="instructor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
