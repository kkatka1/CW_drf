# Generated by Django 5.2.1 on 2025-05-18 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="periodicy",
            new_name="periodicity",
        ),
    ]
