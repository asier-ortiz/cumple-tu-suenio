# Generated by Django 3.0.4 on 2020-05-08 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_producto_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='puede_ser_comprado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='puede_ser_vendido',
        ),
    ]