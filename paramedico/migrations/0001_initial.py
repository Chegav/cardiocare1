# Generated by Django 3.2.5 on 2021-07-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paramedico',
            fields=[
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(max_length=11)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('fechanacimiento', models.DateField()),
                ('tiposangre', models.CharField(max_length=4)),
                ('fechaingreso', models.DateTimeField(auto_now_add=True)),
                ('fechasalida', models.DateTimeField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.BooleanField(default=True)),
                ('contrasena', models.CharField(max_length=40)),
            ],
        ),
    ]
