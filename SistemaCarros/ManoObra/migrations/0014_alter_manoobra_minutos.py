# Generated by Django 3.2.12 on 2022-04-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManoObra', '0013_remove_manoobra_tarifa_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manoobra',
            name='minutos',
            field=models.IntegerField(default=0),
        ),
    ]
