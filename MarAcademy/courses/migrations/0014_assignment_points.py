# Generated by Django 5.1.1 on 2024-11-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0013_assignmentresources_text_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignment",
            name="points",
            field=models.CharField(default="Not graded", max_length=300, null=True),
        ),
    ]