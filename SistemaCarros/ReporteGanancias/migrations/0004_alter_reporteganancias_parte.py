# Generated by Django 3.2.10 on 2022-03-14 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_inventory_quantityinventory'),
        ('ReporteGanancias', '0003_alter_reporteganancias_parte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporteganancias',
            name='parte',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory'),
        ),
    ]
