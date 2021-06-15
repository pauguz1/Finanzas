from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import BalanceGeneral, EstadoResultados
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


#pagina de inicio
def index(request):
    #guardamos la lista de balance general del usuario en especifico
    balance=''
    estadoResultados=''
    if str(request.user) != 'AnonymousUser':
        balance = BalanceGeneral.objects.filter(creador=request.user)
        estadoResultados=EstadoResultados.objects.filter(creador=request.user)
    contexto={
        'listaBalance':balance,
        'listaEstadoResultados':estadoResultados
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
        balance=''
        estadoResultados=''
        if str(request.user) != 'AnonymousUser':
            balance = BalanceGeneral.objects.filter(creador=request.user)
            estadoResultados=EstadoResultados.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        'listaEstadoResultados':estadoResultados
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
        balance=''
        estadoResultados=''
        if str(request.user) != 'AnonymousUser':
            balance = BalanceGeneral.objects.filter(creador=request.user)
            estadoResultados=EstadoResultados.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        'listaEstadoResultados':estadoResultados
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
        balance=''
        estadoResultados=''
        if str(request.user) != 'AnonymousUser':
            balance = BalanceGeneral.objects.filter(creador=request.user)
            estadoResultados=EstadoResultados.objects.filter(creador=request.user)
        contexto={
        'listaBalance':balance,
        'listaEstadoResultados':estadoResultados
        }
        return render(request,'gestion/index.html',contexto)
    


#---------------------------------------------------------------- Estado de resultados --------------------------------------------
# crear balance
@login_required
def crearEstadoResultados(request):
    
    if request.method == 'GET':
        contexto = {
            
        }
        return render(request,'gestion/estadoResultados.html',contexto)

    elif request.method == 'POST':
        ventas= request.POST['ventas']
        devolucionesVentas = request.POST['devolucionesVentas']
        descuentosVentas = request.POST['descuentosVentas']
        bonifRebVentas = request.POST['bonifRebVentas']
        inventarioInicial = request.POST['inventarioInicial']


  
        compras = request.POST['compras']
        fletesCompras = request.POST['fletesCompras']
        gastosImportacion = request.POST['gastosImportacion']

        devolucionesCompras = request.POST['devolucionesCompras']
        descuentosCompras = request.POST['descuentosCompras']
        bonificacionCompras = request.POST['bonificacionCompras']

        inventarioFinal = request.POST['inventarioFinal']

        sueldoVendedores = request.POST['sueldoVendedores']
        comisionVenta = request.POST['comisionVenta']
        propaganda = request.POST['propaganda']
        impuestosMunicipales = request.POST['impuestosMunicipales']

        gastosAlquiler = request.POST['gastosAlquiler']
        gastosGenerales = request.POST['gastosGenerales']
        sueldoAdministracion = request.POST['sueldoAdministracion']
        perdidasCuentasMalas = request.POST['perdidasCuentasMalas']

        alquileresGanados = request.POST['alquileresGanados']
        interesesGanados = request.POST['interesesGanados']
        comisionesGanadas = request.POST['comisionesGanadas']

        interesesGastos = request.POST['interesesGastos']
        perdidasVentas = request.POST['perdidasVentas']
        perdidaEnRoboMercancia = request.POST['perdidaEnRoboMercancia']


     
        fechaCreacion = request.POST['fechaCreacion']

        estado = EstadoResultados()
        estado.pk

        estado.ventas = ventas if ventas != '' else 0
        estado.devolucionesVentas = devolucionesVentas if devolucionesVentas != '' else 0
        estado.descuentosVentas = descuentosVentas if descuentosVentas != '' else 0
        estado.bonifRebVentas = bonifRebVentas  if bonifRebVentas != '' else 0
        estado.inventarioInicial = inventarioInicial if inventarioInicial != '' else 0

        estado.compras = compras if compras != '' else 0
        estado.fletesCompras = fletesCompras if fletesCompras != '' else 0
        estado.gastosImportacion = gastosImportacion if gastosImportacion != '' else 0
        estado.devolucionesCompras = devolucionesCompras if devolucionesCompras != '' else 0

        estado.descuentosCompras = descuentosCompras if descuentosCompras != '' else 0
        estado.bonificacionCompras = bonificacionCompras if bonificacionCompras != '' else 0
        estado.inventarioFinal = inventarioFinal if inventarioFinal != '' else 0

        estado.sueldoVendedores = sueldoVendedores if sueldoVendedores != '' else 0
        estado.comisionVenta = comisionVenta if comisionVenta != '' else 0
        estado.propaganda = propaganda if propaganda != '' else 0
        estado.impuestosMunicipales = impuestosMunicipales if impuestosMunicipales != '' else 0
        estado.gastosAlquiler = gastosAlquiler if gastosAlquiler != '' else 0
        estado.gastosGenerales = gastosGenerales if gastosGenerales != '' else 0
        estado.sueldoAdministracion = sueldoAdministracion if sueldoAdministracion != '' else 0
        estado.perdidasCuentasMalas = perdidasCuentasMalas if perdidasCuentasMalas != '' else 0

        estado.alquileresGanados = alquileresGanados if alquileresGanados != '' else 0
        estado.interesesGanados = interesesGanados if interesesGanados != '' else 0
        estado.comisionesGanadas = comisionesGanadas if comisionesGanadas != '' else 0

        estado.interesesGastos = interesesGastos if interesesGastos != '' else 0
        estado.perdidasVentas = perdidasVentas if perdidasVentas != '' else 0
        estado.perdidaEnRoboMercancia = perdidaEnRoboMercancia if perdidaEnRoboMercancia != '' else 0

        estado.fechaCreacion = fechaCreacion if fechaCreacion != '' else datetime.now()

        estado.creador=request.user
        estado.save()

        balance=''
        estadoResultados=''
        if str(request.user) != 'AnonymousUser':
            balance = BalanceGeneral.objects.filter(creador=request.user)
            estadoResultados=EstadoResultados.objects.filter(creador=request.user)
        contexto={
            'listaBalance':balance,
            'listaEstadoResultados':estadoResultados
        }
        return render(request,'gestion/index.html',contexto)
    
# obtener el detalle del balance
@login_required
def detalleEstadoResultados(request,pk):
    try:
        estadoResultados = EstadoResultados.objects.get(pk=pk)
    except EstadoResultados.DoesNotExist:
        raise Http404("!el Estado de resultados no existe")
    contexto={
        'e':estadoResultados
    }
    return render(request,'gestion/detalleEstadoResultados.html',contexto)


# actualizar balance
@login_required
def actualizarEstadoResultados(request,pk):

    if request.method == 'GET':
        try:
            estado = EstadoResultados.objects.get(pk=pk)
        except EstadoResultados.DoesNotExist:
            raise Http404("!el balance no existe")
        contexto={
            'e':estado
        }
        return render(request,'gestion/actualizarEstadoResultados.html',contexto)

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

