# Generated by Django 4.0.4 on 2022-05-07 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0019_alter_solicitud_revision_archivoadjunto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud_revision',
            name='id_coordinacionSeccion',
        ),
    ]
