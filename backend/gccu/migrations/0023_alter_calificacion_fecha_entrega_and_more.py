# Generated by Django 4.0.4 on 2022-05-08 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0022_alter_evaluacion_id_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='fecha_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='id_observacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gccu.observacion'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='nota',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]