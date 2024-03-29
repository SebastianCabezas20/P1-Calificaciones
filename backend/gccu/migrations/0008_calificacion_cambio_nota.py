# Generated by Django 4.0.4 on 2022-04-30 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0007_asignatura_asignaturas_planestudio_cambio_fecha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=3, max_digits=4)),
                ('fecha_entrega', models.DateTimeField()),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccu.estudiante')),
                ('id_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccu.evaluacion')),
                ('id_observacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccu.observacion')),
            ],
        ),
        migrations.CreateModel(
            name='Cambio_nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anterior_nota', models.DecimalField(decimal_places=3, max_digits=4)),
                ('actual_nota', models.DecimalField(decimal_places=3, max_digits=4)),
                ('motivo', models.TextField()),
                ('id_calificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gccu.calificacion')),
            ],
        ),
    ]
