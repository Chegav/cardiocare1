# Generated by Django 3.2.5 on 2021-07-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_remove_medico_fechadesalida'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='fechadesalida',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='fechadeingreso',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='medico',
            name='fechadenacimiento',
            field=models.CharField(max_length=10),
        ),
    ]
