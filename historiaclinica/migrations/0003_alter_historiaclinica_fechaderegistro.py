# Generated by Django 3.2.5 on 2021-07-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinica', '0002_auto_20210708_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='fechaderegistro',
            field=models.CharField(max_length=10),
        ),
    ]