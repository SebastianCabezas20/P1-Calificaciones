# Generated by Django 4.0.4 on 2022-05-02 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0014_alter_asignatura_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id_tipoAsignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gccu.tipo_asignatura'),
        ),
    ]
