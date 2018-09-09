# Generated by Django 2.1 on 2018-09-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20180423_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_member',
            name='title',
            field=models.CharField(blank=True, choices=[('Principal Investigator', 'Principal Investigator'), ('Research Staff', 'Research Staff'), ('Postdoc', 'Postdoc'), ('Graduate Student', 'Graduate Student'), ('Research Assistant', 'Research Assistant'), ('Undergraduate Student', 'Undergraduate Student')], max_length=70, null=True, verbose_name='Title'),
        ),
    ]
