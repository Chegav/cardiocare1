# Generated by Django 3.2.5 on 2021-07-08 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historiaclinica',
            fields=[
                ('idhistoria', models.IntegerField(primary_key=True, serialize=False)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tipodeingreso', models.CharField(max_length=1)),
                ('fechaderegistro', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('presion', models.IntegerField(max_length=7)),
                ('cedmedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico')),
                ('cedpaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]
