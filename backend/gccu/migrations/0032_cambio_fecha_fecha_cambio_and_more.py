# Generated by Django 4.0.4 on 2022-06-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0031_alter_evaluacion_ponderacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambio_fecha',
            name='fecha_cambio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='cambio_ponderacion',
            name='fecha_cambio',
            field=models.DateField(null=True),
        ),
    ]
