# Generated by Django 3.2.10 on 2022-02-17 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0011_alter_carro_motor'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='fotosCarro',
            field=models.ImageField(blank=True, null=True, upload_to='fotosCarro/'),
        ),
        migrations.AddField(
            model_name='carro',
            name='garantia',
            field=models.ImageField(blank=True, null=True, upload_to='garantia/'),
        ),
    ]
