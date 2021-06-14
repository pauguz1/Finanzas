from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import BalanceGeneral
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


#pagina de inicio
def index(request):
    #guardamos la lista de balance general del usuario en especifico
    balance=''
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        balance = BalanceGeneral.objects.filter(creador=request.user)
    contexto={
        'listaBalance':balance,
    }
    return render(request,'gestion/index.html',contexto)

#----------------------------------------------------- Balance -------------------------------------

# crear balance
@login_required
def crearBalance(request):
    
    if request.method == 'GET':
        contexto = {
            
        }
        return render(request,'gestion/balance.html',contexto)

    elif request.method == 'POST':
        disponible= request.POST['disponible']
        valoresNegociables = request.POST['valoresNegociables']
        deudoresPorVenta = request.POST['deudoresPorVenta']
        deudoresVarios = request.POST['deudoresVarios']
        impuestosPorRecuperar = request.POST['impuestosPorRecuperar']


        #pasivo circulante
        cuentaPorPagar = request.POST['cuentaPorPagar']
        provedores = request.POST['provedores']
        retenciones = request.POST['retenciones']
        convenioConInstituciones = request.POST['convenioConInstituciones']
        otros = request.POST['otros']

        #activo fijo
        mueblesUtiles = request.POST['mueblesUtiles']
        maquinariaEquipoOficina = request.POST['maquinariaEquipoOficina']
        otrosActivosFijos = request.POST['otrosActivosFijos']
        equipoTransporte = request.POST['equipoTransporte']

        #pasivo fijo
        acredoresHipotecarios = request.POST['acredoresHipotecarios']

        #otros activos
        programasComputacionales = request.POST['programasComputacionales']
        otros2 = request.POST['otros2']
        amortizaciones = request.POST['amortizaciones']

        #capital contable
        capitalSocial = request.POST['capitalSocial']
        utilidadesRetenidas = request.POST['utilidadesRetenidas']

        fechaCreacion = request.POST['fechaCreacion']

        balance = BalanceGeneral()
        balance.pk

        balance.disponible = disponible if disponible != '' else 0
        balance.valoresNegociables = valoresNegociables if valoresNegociables != '' else 0
        balance.deudoresPorVenta = deudoresPorVenta if deudoresPorVenta != '' else 0
        balance.deudoresVarios = deudoresVarios  if deudoresVarios != '' else 0
        balance.impuestosPorRecuperar = impuestosPorRecuperar if impuestosPorRecuperar != '' else 0

        balance.mueblesUtiles = mueblesUtiles if mueblesUtiles != '' else 0
        balance.maquinariaEquipoOficina = maquinariaEquipoOficina if maquinariaEquipoOficina != '' else 0
        balance.otrosActivosFijos = otrosActivosFijos if otrosActivosFijos != '' else 0
        balance.equipoTransporte = equipoTransporte if equipoTransporte != '' else 0

        balance.programasComputacionales = programasComputacionales if programasComputacionales != '' else 0
        balance.otros = otros if otros != '' else 0
        balance.amortizaciones = amortizaciones if amortizaciones != '' else 0

        balance.cuentaPorPagar = cuentaPorPagar if cuentaPorPagar != '' else 0
        balance.provedores = provedores if provedores != '' else 0
        balance.retenciones = retenciones if retenciones != '' else 0
        balance.convenioConInstituciones = convenioConInstituciones if convenioConInstituciones != '' else 0
        balance.otros2 = otros2 if otros2 != '' else 0
        balance.acredoresHipotecarios = acredoresHipotecarios if acredoresHipotecarios != '' else 0
        balance.capitalSocial = capitalSocial if capitalSocial != '' else 0
        balance.utilidadesRetenidas = utilidadesRetenidas if utilidadesRetenidas != '' else 0

        balance.fechaCreacion = fechaCreacion if fechaCreacion != '' else datetime.now()

        balance.creador=request.user
        balance.save()
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)
    
# obtener el detalle del balance
@login_required
def detalleBalance(request,pk):
    try:
        balance = BalanceGeneral.objects.get(pk=pk)
    except BalanceGeneral.DoesNotExist:
        raise Http404("!el balance no existe")
    contexto={
        'b':balance
    }
    return render(request,'gestion/detalleBalance.html',contexto)


# actualizar balance
@login_required
def actualizarBalance(request,pk):

    if request.method == 'GET':
        try:
            balance = BalanceGeneral.objects.get(pk=pk)
        except BalanceGeneral.DoesNotExist:
            raise Http404("!el balance no existe")
        contexto={
            'b':balance
        }
        return render(request,'gestion/actualizarBalance.html',contexto)

    elif request.method == 'POST':
        disponible= request.POST['disponible']
        valoresNegociables = request.POST['valoresNegociables']
        deudoresPorVenta = request.POST['deudoresPorVenta']
        deudoresVarios = request.POST['deudoresVarios']
        impuestosPorRecuperar = request.POST['impuestosPorRecuperar']


        #pasivo circulante
        cuentaPorPagar = request.POST['cuentaPorPagar']
        provedores = request.POST['provedores']
        retenciones = request.POST['retenciones']
        convenioConInstituciones = request.POST['convenioConInstituciones']
        otros = request.POST['otros']

        #activo fijo
        mueblesUtiles = request.POST['mueblesUtiles']
        maquinariaEquipoOficina = request.POST['maquinariaEquipoOficina']
        otrosActivosFijos = request.POST['otrosActivosFijos']
        equipoTransporte = request.POST['equipoTransporte']

        #pasivo fijo
        acredoresHipotecarios = request.POST['acredoresHipotecarios']

        #otros activos
        programasComputacionales = request.POST['programasComputacionales']
        otros2 = request.POST['otros2']
        amortizaciones = request.POST['amortizaciones']

        #capital contable
        capitalSocial = request.POST['capitalSocial']
        utilidadesRetenidas = request.POST['utilidadesRetenidas']

        fechaCreacion = request.POST['fechaCreacion']

        balance = BalanceGeneral.objects.get(id=request.POST['id'])

        balance.disponible = disponible if disponible != '' else 0
        balance.valoresNegociables = valoresNegociables if valoresNegociables != '' else 0
        balance.deudoresPorVenta = deudoresPorVenta if deudoresPorVenta != '' else 0
        balance.deudoresVarios = deudoresVarios  if deudoresVarios != '' else 0
        balance.impuestosPorRecuperar = impuestosPorRecuperar if impuestosPorRecuperar != '' else 0

        balance.mueblesUtiles = mueblesUtiles if mueblesUtiles != '' else 0
        balance.maquinariaEquipoOficina = maquinariaEquipoOficina if maquinariaEquipoOficina != '' else 0
        balance.otrosActivosFijos = otrosActivosFijos if otrosActivosFijos != '' else 0
        balance.equipoTransporte = equipoTransporte if equipoTransporte != '' else 0

        balance.programasComputacionales = programasComputacionales if programasComputacionales != '' else 0
        balance.otros = otros if otros != '' else 0
        balance.amortizaciones = amortizaciones if amortizaciones != '' else 0

        balance.cuentaPorPagar = cuentaPorPagar if cuentaPorPagar != '' else 0
        balance.provedores = provedores if provedores != '' else 0
        balance.retenciones = retenciones if retenciones != '' else 0
        balance.convenioConInstituciones = convenioConInstituciones if convenioConInstituciones != '' else 0
        balance.otros2 = otros2 if otros2 != '' else 0
        balance.acredoresHipotecarios = acredoresHipotecarios if acredoresHipotecarios != '' else 0
        balance.capitalSocial = capitalSocial if capitalSocial != '' else 0
        balance.utilidadesRetenidas = utilidadesRetenidas if utilidadesRetenidas != '' else 0

        balance.fechaCreacion = fechaCreacion if fechaCreacion != '' else datetime.now()

        balance.creador=request.user
        balance.save()
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)

# eliminar balance
@login_required
def eliminarBalance(request,pk):

    if request.method == 'GET':
        try:
            balance = BalanceGeneral.objects.get(pk=pk)
        except BalanceGeneral.DoesNotExist:
            raise Http404("!el balance no existe")
        contexto={
            'b':balance
        }
        return render(request,'gestion/eliminarBalance.html',contexto)

    elif request.method == 'POST':
        balance = BalanceGeneral.objects.get(id=request.POST['id'])
        balance.delete()
        #eliminamos el registro
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)
    


#---------------------------------------------------------------- Estado de resultados --------------------------------------------
# crear balance
@login_required
def crearEstadoResultados(request):
    
    if request.method == 'GET':
        contexto = {
            
        }
        return render(request,'gestion/balance.html',contexto)

    elif request.method == 'POST':
        disponible= request.POST['disponible']
        valoresNegociables = request.POST['valoresNegociables']
        deudoresPorVenta = request.POST['deudoresPorVenta']
        deudoresVarios = request.POST['deudoresVarios']
        impuestosPorRecuperar = request.POST['impuestosPorRecuperar']


        #pasivo circulante
        cuentaPorPagar = request.POST['cuentaPorPagar']
        provedores = request.POST['provedores']
        retenciones = request.POST['retenciones']
        convenioConInstituciones = request.POST['convenioConInstituciones']
        otros = request.POST['otros']

        #activo fijo
        mueblesUtiles = request.POST['mueblesUtiles']
        maquinariaEquipoOficina = request.POST['maquinariaEquipoOficina']
        otrosActivosFijos = request.POST['otrosActivosFijos']
        equipoTransporte = request.POST['equipoTransporte']

        #pasivo fijo
        acredoresHipotecarios = request.POST['acredoresHipotecarios']

        #otros activos
        programasComputacionales = request.POST['programasComputacionales']
        otros2 = request.POST['otros2']
        amortizaciones = request.POST['amortizaciones']

        #capital contable
        capitalSocial = request.POST['capitalSocial']
        utilidadesRetenidas = request.POST['utilidadesRetenidas']

        fechaCreacion = request.POST['fechaCreacion']

        balance = BalanceGeneral()
        balance.pk

        balance.disponible = disponible if disponible != '' else 0
        balance.valoresNegociables = valoresNegociables if valoresNegociables != '' else 0
        balance.deudoresPorVenta = deudoresPorVenta if deudoresPorVenta != '' else 0
        balance.deudoresVarios = deudoresVarios  if deudoresVarios != '' else 0
        balance.impuestosPorRecuperar = impuestosPorRecuperar if impuestosPorRecuperar != '' else 0

        balance.mueblesUtiles = mueblesUtiles if mueblesUtiles != '' else 0
        balance.maquinariaEquipoOficina = maquinariaEquipoOficina if maquinariaEquipoOficina != '' else 0
        balance.otrosActivosFijos = otrosActivosFijos if otrosActivosFijos != '' else 0
        balance.equipoTransporte = equipoTransporte if equipoTransporte != '' else 0

        balance.programasComputacionales = programasComputacionales if programasComputacionales != '' else 0
        balance.otros = otros if otros != '' else 0
        balance.amortizaciones = amortizaciones if amortizaciones != '' else 0

        balance.cuentaPorPagar = cuentaPorPagar if cuentaPorPagar != '' else 0
        balance.provedores = provedores if provedores != '' else 0
        balance.retenciones = retenciones if retenciones != '' else 0
        balance.convenioConInstituciones = convenioConInstituciones if convenioConInstituciones != '' else 0
        balance.otros2 = otros2 if otros2 != '' else 0
        balance.acredoresHipotecarios = acredoresHipotecarios if acredoresHipotecarios != '' else 0
        balance.capitalSocial = capitalSocial if capitalSocial != '' else 0
        balance.utilidadesRetenidas = utilidadesRetenidas if utilidadesRetenidas != '' else 0

        balance.fechaCreacion = fechaCreacion if fechaCreacion != '' else datetime.now()

        balance.creador=request.user
        balance.save()
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)
    
# obtener el detalle del balance
@login_required
def detalleEstadoResultados(request,pk):
    try:
        balance = BalanceGeneral.objects.get(pk=pk)
    except BalanceGeneral.DoesNotExist:
        raise Http404("!el balance no existe")
    contexto={
        'b':balance
    }
    return render(request,'gestion/detalleBalance.html',contexto)


# actualizar balance
@login_required
def actualizarEstadoResultados(request,pk):

    if request.method == 'GET':
        try:
            balance = BalanceGeneral.objects.get(pk=pk)
        except BalanceGeneral.DoesNotExist:
            raise Http404("!el balance no existe")
        contexto={
            'b':balance
        }
        return render(request,'gestion/actualizarBalance.html',contexto)

    elif request.method == 'POST':
        disponible= request.POST['disponible']
        valoresNegociables = request.POST['valoresNegociables']
        deudoresPorVenta = request.POST['deudoresPorVenta']
        deudoresVarios = request.POST['deudoresVarios']
        impuestosPorRecuperar = request.POST['impuestosPorRecuperar']


        #pasivo circulante
        cuentaPorPagar = request.POST['cuentaPorPagar']
        provedores = request.POST['provedores']
        retenciones = request.POST['retenciones']
        convenioConInstituciones = request.POST['convenioConInstituciones']
        otros = request.POST['otros']

        #activo fijo
        mueblesUtiles = request.POST['mueblesUtiles']
        maquinariaEquipoOficina = request.POST['maquinariaEquipoOficina']
        otrosActivosFijos = request.POST['otrosActivosFijos']
        equipoTransporte = request.POST['equipoTransporte']

        #pasivo fijo
        acredoresHipotecarios = request.POST['acredoresHipotecarios']

        #otros activos
        programasComputacionales = request.POST['programasComputacionales']
        otros2 = request.POST['otros2']
        amortizaciones = request.POST['amortizaciones']

        #capital contable
        capitalSocial = request.POST['capitalSocial']
        utilidadesRetenidas = request.POST['utilidadesRetenidas']

        fechaCreacion = request.POST['fechaCreacion']

        balance = BalanceGeneral.objects.get(id=request.POST['id'])

        balance.disponible = disponible if disponible != '' else 0
        balance.valoresNegociables = valoresNegociables if valoresNegociables != '' else 0
        balance.deudoresPorVenta = deudoresPorVenta if deudoresPorVenta != '' else 0
        balance.deudoresVarios = deudoresVarios  if deudoresVarios != '' else 0
        balance.impuestosPorRecuperar = impuestosPorRecuperar if impuestosPorRecuperar != '' else 0

        balance.mueblesUtiles = mueblesUtiles if mueblesUtiles != '' else 0
        balance.maquinariaEquipoOficina = maquinariaEquipoOficina if maquinariaEquipoOficina != '' else 0
        balance.otrosActivosFijos = otrosActivosFijos if otrosActivosFijos != '' else 0
        balance.equipoTransporte = equipoTransporte if equipoTransporte != '' else 0

        balance.programasComputacionales = programasComputacionales if programasComputacionales != '' else 0
        balance.otros = otros if otros != '' else 0
        balance.amortizaciones = amortizaciones if amortizaciones != '' else 0

        balance.cuentaPorPagar = cuentaPorPagar if cuentaPorPagar != '' else 0
        balance.provedores = provedores if provedores != '' else 0
        balance.retenciones = retenciones if retenciones != '' else 0
        balance.convenioConInstituciones = convenioConInstituciones if convenioConInstituciones != '' else 0
        balance.otros2 = otros2 if otros2 != '' else 0
        balance.acredoresHipotecarios = acredoresHipotecarios if acredoresHipotecarios != '' else 0
        balance.capitalSocial = capitalSocial if capitalSocial != '' else 0
        balance.utilidadesRetenidas = utilidadesRetenidas if utilidadesRetenidas != '' else 0

        balance.fechaCreacion = fechaCreacion if fechaCreacion != '' else datetime.now()

        balance.creador=request.user
        balance.save()
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)

# eliminar balance
@login_required
def eliminarEstadoResultados(request,pk):

    if request.method == 'GET':
        try:
            balance = BalanceGeneral.objects.get(pk=pk)
        except BalanceGeneral.DoesNotExist:
            raise Http404("!el balance no existe")
        contexto={
            'b':balance
        }
        return render(request,'gestion/eliminarBalance.html',contexto)

    elif request.method == 'POST':
        balance = BalanceGeneral.objects.get(id=request.POST['id'])
        balance.delete()
        #eliminamos el registro
        balance = BalanceGeneral.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        }
        return render(request,'gestion/index.html',contexto)

