# Generated by Django 3.0.3 on 2020-06-20 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200620_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrafield',
            name='title',
        ),
    ]