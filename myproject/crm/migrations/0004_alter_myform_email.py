# Generated by Django 5.1.6 on 2025-02-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_myform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myform",
            name="Email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
