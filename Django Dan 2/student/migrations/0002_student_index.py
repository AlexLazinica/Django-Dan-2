# Generated by Django 4.2.5 on 2023-09-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"), #zavisnost od 0001
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="index",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
