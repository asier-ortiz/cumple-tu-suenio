# Generated by Django 3.0.4 on 2020-03-12 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0002_auto_20200312_1130'),
        ('Empleados', '0005_auto_20200312_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('nif', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=30)),
                ('provincia', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('Imagen', models.ImageField(blank=True, default='/user.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ventas.Cliente')),
                ('comercial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Empleados.Empleado')),
                ('productos', models.ManyToManyField(to='Inventario.Producto')),
            ],
        ),
    ]
