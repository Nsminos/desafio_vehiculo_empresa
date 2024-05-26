# Generated by Django 4.2 on 2024-05-22 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('activo', models.BooleanField()),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroContabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('valor', models.FloatField()),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('vehiculo_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='contabilidad', to='app.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('vehiculo_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='chofer', to='app.vehiculo')),
            ],
        ),
    ]
