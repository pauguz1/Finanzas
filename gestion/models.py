from django.db import models
from django.conf import settings
from datetime import date, datetime
# Create your models here.

# modelo para el balace general
class BalanceGeneral(models.Model):
    #activo circulante
    disponible = models.FloatField(default=0)
    valoresNegociables = models.FloatField(default=0)
    deudoresPorVenta = models.FloatField(default=0)
    deudoresVarios = models.FloatField(default=0)
    impuestosPorRecuperar = models.FloatField(default=0)


    #pasivo circulante
    cuentaPorPagar = models.FloatField(default=0)
    provedores = models.FloatField(default=0)
    retenciones = models.FloatField(default=0)
    convenioConInstituciones = models.FloatField(default=0)
    otros = models.FloatField(default=0)

    #activo fijo
    mueblesUtiles = models.FloatField(default=0)
    maquinariaEquipoOficina = models.FloatField(default=0)
    otrosActivosFijos = models.FloatField(default=0)
    equipoTransporte = models.FloatField(default=0)

    #pasivo fijo
    acredoresHipotecarios = models.FloatField(default=0)

    #otros activos
    programasComputacionales = models.FloatField(default=0)
    otros2 = models.FloatField(default=0)
    amortizaciones = models.FloatField(default=0)

    #capital contable
    capitalSocial = models.FloatField(default=0)
    utilidadesRetenidas = models.FloatField(default=0)

    fechaCreacion = models.DateField(default=datetime.now)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.creador,self.fechaCreacion)

# modelo para el estado de resultados
class EstadoResultados(models.Model):
    #activo circulante 28 campos en total
    ventas = models.FloatField(default=0)
    devolucionesVentas = models.FloatField(default=0)
    descuentosVentas = models.FloatField(default=0)
    bonifRebVentas = models.FloatField(default=0)

    inventarioInicial = models.FloatField(default=0)
    compras = models.FloatField(default=0)
    fletesCompras = models.FloatField(default=0)
    gastosImportacion = models.FloatField(default=0)

    devolucionesCompras = models.FloatField(default=0)
    descuentosCompras = models.FloatField(default=0)
    bonificacionCompras = models.FloatField(default=0)

    inventarioFinal = models.FloatField(default=0)

    sueldoVendedores = models.FloatField(default=0)
    comisionVenta = models.FloatField(default=0)
    propaganda = models.FloatField(default=0)
    impuestosMunicipales = models.FloatField(default=0)

    gastosAlquiler = models.FloatField(default=0)
    gastosGenerales = models.FloatField(default=0)
    sueldoAdministracion = models.FloatField(default=0)
    perdidasCuentasMalas = models.FloatField(default=0)

    alquileresGanados = models.FloatField(default=0)
    interesesGanados = models.FloatField(default=0)
    comisionesGanadas = models.FloatField(default=0)

    interesesGastos = models.FloatField(default=0)
    perdidasVentas = models.FloatField(default=0)
    perdidaEnRoboMercancia = models.FloatField(default=0)

    fechaCreacion = models.DateField(default=datetime.now)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.creador,self.fechaCreacion)


# modelo para el tipo de empleado
class TipoEmpleado(models.Model):
    #activo circulante 28 campos en total
    nombre = models.CharField(max_length=50)
    salario = models.FloatField(default=0)
    descripcion = models.CharField(max_length=60)
    def __str__(self):
        return '{}'.format(self.nombre)

# modelo para el tipo de empleado
class Empleado(models.Model):
    #activo circulante 28 campos en total
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=40)
    ap_materno = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fechaCreacion = models.DateField(default=datetime.now)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # para las horas que va a trabajar
    horas = models.IntegerField()
    puesto = models.ForeignKey(TipoEmpleado,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)
