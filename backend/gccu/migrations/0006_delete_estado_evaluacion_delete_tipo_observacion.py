# Generated by Django 4.0.4 on 2022-04-29 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0005_estado_evaluacion_tipo_observacion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estado_Evaluacion',
        ),
        migrations.DeleteModel(
            name='Tipo_Observacion',
        ),
    ]
