# Generated by Django 3.2.10 on 2022-02-14 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0003_remove_presupuestos_citado_por'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuestos',
            name='ajustado_por',
        ),
        migrations.RemoveField(
            model_name='presupuestos',
            name='condiciones_servicio',
        ),
        migrations.RemoveField(
            model_name='presupuestos',
            name='equilibrado',
        ),
        migrations.RemoveField(
            model_name='presupuestos',
            name='garantia',
        ),
        migrations.RemoveField(
            model_name='presupuestos',
            name='realizado_por',
        ),
    ]
