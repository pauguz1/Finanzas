from django.db import models
from django.conf import settings
from datetime import date, datetime
# Create your models here.

class BalanceGeneral(models.Model):
    #activo circulante
    disponible = models.FloatField()
    valoresNegociables = models.FloatField()
    deudoresPorVenta = models.FloatField()
    deudoresVarios = models.FloatField()
    impuestosPorRecuperar = models.FloatField()


    #pasivo circulante
    cuentaPorPagar = models.FloatField()
    proviciones = models.FloatField()
    retenciones = models.FloatField()
    convenioConInstituciones = models.FloatField()
    otros = models.FloatField()

    #activo fijo
    mueblesUtiles = models.FloatField()
    maquinariaEquipoOficina = models.FloatField()
    otrosActivosFijos = models.FloatField()
    equipoTransporte = models.FloatField()

    #pasivo fijo
    acredoresHipotecarios = models.FloatField()

    #otros activos
    programasComputacionales = models.FloatField()
    otros2 = models.FloatField()
    amortizaciones = models.FloatField()

    #capital contable
    capitalSocial = models.FloatField()
    utilidadesRetenidas = models.FloatField()

    fechaCreacion = models.DateField(default=datetime.now)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.creador,self.fechaCreacion)
