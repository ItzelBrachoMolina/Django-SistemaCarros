# Generated by Django 3.2.9 on 2021-12-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0011_auto_20211209_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='apellido',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='social_media3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipo',
            field=models.CharField(max_length=200),
        ),
    ]
