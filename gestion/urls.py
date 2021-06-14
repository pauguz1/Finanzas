


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
    
    path('crear/estadoresultados',views.crearBalance,name='crearEstadoResultados'),
    path('detalle/estadoresultados/<int:pk>',views.detalleBalance,name='detalleEstadoResultados'),
    path('actualizar/estadoresultados/<int:pk>',views.actualizarBalance,name='actualizarEstadoResultados'),
    path('eliminar/estadoresultados/<int:pk>',views.eliminarBalance,name='eliminarEstadoResultados')
]