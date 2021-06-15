


from django.contrib import admin
from django.urls import path
from . import views


app_name='gestion'
urlpatterns=[
    path('',views.index,name='index'),
    path('crear/empleado',views.index,name='index2'),

    path('crear/balance',views.crearBalance,name='crearBalance'),
    path('detalle/balance/<int:pk>',views.detalleBalance,name='detalleBalance'),
    path('actualizar/balance/<int:pk>',views.actualizarBalance,name='actualizarBalance'),
    path('eliminar/balance/<int:pk>',views.eliminarBalance,name='eliminarBalance'),
    
    path('crear/estadoresultados',views.crearEstadoResultados,name='crearEstadoResultados'),
    path('detalle/estadoresultados/<int:pk>',views.detalleEstadoResultados,name='detalleEstadoResultados'),
    path('actualizar/estadoresultados/<int:pk>',views.actualizarEstadoResultados,name='actualizarEstadoResultados'),
    path('eliminar/estadoresultados/<int:pk>',views.eliminarEstadoResultados,name='eliminarEstadoResultados'),

    path('factibilidad/',views.factibilidad,name="factibilidad"),
    path('detalle/empleado/<int:pk>',views.detalleEmpleado,name="detalleEmpleado"),
    path('actualizar/empleado/<int:pk>',views.actualizarEmpleado,name="actualizarEmpleado"),
    path('eliminar/empleado/<int:pk>',views.eliminarEmpleado,name="eliminarEmpleado")
]