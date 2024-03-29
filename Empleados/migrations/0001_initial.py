# Generated by Django 3.0.4 on 2020-03-08 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_contratacion', models.DateField()),
                ('fotografia', models.BinaryField(blank=True)),
                ('nacionalidad', models.CharField(max_length=15)),
                ('dni', models.CharField(max_length=9)),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')], max_length=10)),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorciado', 'Divorciado')], max_length=10)),
                ('fecha_nacimiento', models.DateField()),
                ('horas_semanales', models.IntegerField()),
                ('coste_partes_horas', models.FloatField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.Departamento')),
            ],
        ),
    ]
