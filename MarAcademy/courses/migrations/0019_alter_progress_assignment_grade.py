# Generated by Django 5.1.1 on 2024-11-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0018_progress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="progress",
            name="assignment_grade",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
