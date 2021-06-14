from django.db import models
from django.conf import settings
from datetime import date, datetime
# Create your models here.

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
