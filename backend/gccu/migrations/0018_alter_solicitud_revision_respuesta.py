# Generated by Django 4.0.4 on 2022-05-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0017_solicitud_revision_id_coordinacionseccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_revision',
            name='respuesta',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
