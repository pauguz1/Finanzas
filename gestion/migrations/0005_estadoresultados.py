# Generated by Django 3.2.3 on 2021-06-14 20:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0004_auto_20210614_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoResultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventas', models.FloatField(default=0)),
                ('devolucionesVentas', models.FloatField(default=0)),
                ('descuentosVentas', models.FloatField(default=0)),
                ('bonifRebVentas', models.FloatField(default=0)),
                ('inventarioInicial', models.FloatField(default=0)),
                ('compras', models.FloatField(default=0)),
                ('fletesCompras', models.FloatField(default=0)),
                ('gastosImportacion', models.FloatField(default=0)),
                ('devolucionesCompras', models.FloatField(default=0)),
                ('descuentosCompras', models.FloatField(default=0)),
                ('bonificacionCompras', models.FloatField(default=0)),
                ('inventarioFinal', models.FloatField(default=0)),
                ('sueldoVendedores', models.FloatField(default=0)),
                ('comisionVenta', models.FloatField(default=0)),
                ('propaganda', models.FloatField(default=0)),
                ('impuestosMunicipales', models.FloatField(default=0)),
                ('gastosAlquiler', models.FloatField(default=0)),
                ('gastosGenerales', models.FloatField(default=0)),
                ('sueldoAdministracion', models.FloatField(default=0)),
                ('perdidasCuentasMalas', models.FloatField(default=0)),
                ('alquileresGanados', models.FloatField(default=0)),
                ('interesesGanados', models.FloatField(default=0)),
                ('comisionesGanadas', models.FloatField(default=0)),
                ('interesesGastos', models.FloatField(default=0)),
                ('perdidasVentas', models.FloatField(default=0)),
                ('perdidaEnRoboMercancia', models.FloatField(default=0)),
                ('fechaCreacion', models.DateField(default=datetime.datetime.now)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
