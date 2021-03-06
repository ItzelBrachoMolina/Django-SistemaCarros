# Generated by Django 3.2.10 on 2022-02-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('dealer', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_number', models.IntegerField()),
                ('status', models.CharField(default='0', max_length=255)),
            ],
        ),
    ]
