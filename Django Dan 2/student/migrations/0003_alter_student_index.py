# Generated by Django 4.2.5 on 2023-09-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_student_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="index",
            field=models.CharField(db_index=True, default=0, max_length=50),
            preserve_default=False,
        ),
    ]
