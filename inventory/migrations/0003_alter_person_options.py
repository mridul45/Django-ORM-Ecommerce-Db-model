# Generated by Django 4.1 on 2022-08-28 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_person"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="person",
            options={"ordering": ("first_name",)},
        ),
    ]
