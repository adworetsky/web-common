# Generated by Django 2.0.3 on 2018-04-21 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0006_delete_job_listing"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news_item",
            old_name="date",
            new_name="pub_date",
        ),
    ]
