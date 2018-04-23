# Generated by Django 2.0.3 on 2018-04-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_publication_link_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_item',
            name='title',
            field=models.CharField(max_length=350, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='publication_link',
            name='name',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Name'),
        ),
    ]
