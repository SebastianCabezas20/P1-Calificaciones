# Generated by Django 4.0.4 on 2022-05-02 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0012_evaluacion_id_coordinacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id_coordinador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gccu.coordinador'),
        ),
    ]
