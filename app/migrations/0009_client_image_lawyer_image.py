# Generated by Django 4.2.11 on 2024-04-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="lawyer",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
