# Generated by Django 4.0.4 on 2022-05-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0013_alter_asignatura_id_coordinador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]