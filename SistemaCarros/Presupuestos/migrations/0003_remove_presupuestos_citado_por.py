# Generated by Django 3.2.10 on 2022-02-14 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0002_auto_20220213_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuestos',
            name='citado_por',
        ),
    ]
