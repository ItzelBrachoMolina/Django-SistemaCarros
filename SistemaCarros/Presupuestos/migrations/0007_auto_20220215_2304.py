# Generated by Django 3.2.10 on 2022-02-16 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0006_auto_20220213_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuestos',
            name='session_hash',
        ),
        migrations.RemoveField(
            model_name='presupuestos',
            name='stage',
        ),
    ]
