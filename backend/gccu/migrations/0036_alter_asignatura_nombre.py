# Generated by Django 4.0.4 on 2022-06-29 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0035_alter_calificacion_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
    ]