# Generated by Django 4.0.4 on 2022-05-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0010_coordinador_dig_verificador_coordinador_rut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='isAutogestionada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='isMBI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coordinacion_seccion',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='semestre',
            name='isActual',
            field=models.BooleanField(default=False),
        ),
    ]
