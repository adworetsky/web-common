# Generated by Django 2.0.3 on 2018-04-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0007_auto_20180421_1224"),
    ]

    operations = [
        migrations.AddField(
            model_name="publication_link",
            name="name",
            field=models.CharField(
                blank=True, max_length=350, null=True, unique=True, verbose_name="Name"
            ),
        ),
    ]
