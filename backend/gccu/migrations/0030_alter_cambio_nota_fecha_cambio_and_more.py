# Generated by Django 4.0.4 on 2022-05-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0029_remove_calificacion_id_observacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cambio_nota',
            name='fecha_cambio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='solicitud_revision',
            name='fecha_creacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='solicitud_revision',
            name='fecha_respuesta',
            field=models.DateField(blank=True, default=0, null=True),
        ),
    ]
