# Generated by Django 5.1.1 on 2024-11-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0012_assignmentresources"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignmentresources",
            name="text",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="assignmentrequirement",
            name="requirement_text",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
