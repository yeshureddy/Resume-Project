# Generated by Django 3.0.3 on 2020-06-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_skills_workexp'),
    ]

    operations = [
        migrations.CreateModel(
            name='extrafield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('explanation', models.CharField(max_length=5000)),
            ],
        ),
    ]