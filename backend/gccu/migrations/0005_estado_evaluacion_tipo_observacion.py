# Generated by Django 4.0.4 on 2022-04-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gccu', '0004_delete_estado_evaluacion_delete_tipo_observacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('siglas', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]