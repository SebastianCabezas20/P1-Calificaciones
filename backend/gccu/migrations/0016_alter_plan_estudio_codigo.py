# Generated by Django 4.0.4 on 2022-05-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0015_alter_asignatura_id_tipoasignatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_estudio',
            name='codigo',
            field=models.CharField(max_length=10),
        ),
    ]