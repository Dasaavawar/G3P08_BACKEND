# Generated by Django 3.2.8 on 2021-10-08 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthAppEmpleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCapacitacion',
            fields=[
                ('idAreaCap', models.AutoField(primary_key=True, serialize=False, verbose_name='id_area_capacitacion')),
                ('area', models.CharField(max_length=45, verbose_name='area')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('idCapacitacion', models.AutoField(primary_key=True, serialize=False, verbose_name='id_capacitacion')),
                ('curso', models.CharField(max_length=45, verbose_name='curso')),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
                ('idAreaCapacitacionFk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='capacitacion_area_fk', to='AuthAppEmpleados.areacapacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('idCargo', models.AutoField(primary_key=True, serialize=False, verbose_name='id_cargo')),
                ('cargo', models.CharField(max_length=45, verbose_name='cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('cedula', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='cedula')),
                ('nombres', models.CharField(max_length=50, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('cargoIdFk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cargo_id_fk', to='AuthAppEmpleados.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idRegistro', models.AutoField(primary_key=True, serialize=False, verbose_name='id_registro')),
                ('cedulaTrabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cedula_trabajador', to='AuthAppEmpleados.trabajadores')),
                ('idCapacitacionFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_capacitacion_fk', to='AuthAppEmpleados.capacitacion')),
            ],
        ),
        migrations.CreateModel(
            name='CargosCapacitacion',
            fields=[
                ('idCarCap', models.AutoField(primary_key=True, serialize=False, verbose_name='id_car_cap')),
                ('idAreaCapFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_area_fk', to='AuthAppEmpleados.areacapacitacion')),
                ('idcarFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_cargo_fk', to='AuthAppEmpleados.cargos')),
            ],
        ),
    ]
