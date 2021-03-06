# Generated by Django 3.2.9 on 2021-12-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0010_auto_20211208_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='ciudad',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contacto_alternativo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contacto_alternativo2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='contacto_alternativo3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='corporacion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='estado',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fax',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='pais',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media2',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media3',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='website',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
