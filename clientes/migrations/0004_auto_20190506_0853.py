# Generated by Django 2.2 on 2019-05-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190502_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='salario',
            field=models.CharField(max_length=30),
        ),
    ]
