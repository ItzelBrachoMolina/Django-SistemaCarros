# Generated by Django 3.2.12 on 2022-03-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0009_auto_20220328_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestos',
            name='resume',
            field=models.CharField(default=0, max_length=255),
        ),
    ]