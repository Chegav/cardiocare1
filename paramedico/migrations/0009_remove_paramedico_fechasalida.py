# Generated by Django 3.2.5 on 2021-07-08 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paramedico', '0008_alter_paramedico_fechasalida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paramedico',
            name='fechasalida',
        ),
    ]
