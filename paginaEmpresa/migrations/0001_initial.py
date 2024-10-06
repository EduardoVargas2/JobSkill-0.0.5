# Generated by Django 5.1 on 2024-10-06 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobskill1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePuesto', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=255)),
                ('requisitos', models.CharField(max_length=255)),
                ('sueldoBase', models.FloatField()),
                ('beneficios', models.CharField(blank=True, max_length=255, null=True)),
                ('disponibles', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobskill1.empresa')),
            ],
            options={
                'verbose_name': 'puesto',
                'verbose_name_plural': 'puestos',
            },
        ),
    ]
