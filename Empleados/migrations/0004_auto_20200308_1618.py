# Generated by Django 3.0.4 on 2020-03-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0003_auto_20200308_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fotografia',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to=''),
        ),
    ]