# Generated by Django 4.2.11 on 2024-04-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qa", "0002_alter_question_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
