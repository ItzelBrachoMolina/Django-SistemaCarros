# Generated by Django 3.2.7 on 2021-10-07 18:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManoObra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reclamo_no', models.IntegerField()),
                ('notas', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('que_hara', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ManoObra.manoobra')),
            ],
        ),
    ]
