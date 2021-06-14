


from django.contrib import admin
from django.urls import path
from . import views


app_name='gestion'
urlpatterns=[
    path('',views.index,name='index'),
    path('crear/estadoresultados',views.index,name='index0'),
    path('crear/balance',views.crearBalance,name='crearBalance'),
    path('crear/empleado',views.index,name='index2'),
    path('detalle/balance/<int:pk>',views.detalleBalance,name='detalleBalance'),
    path('actualizar/balance/<int:pk>',views.actualizarBalance,name='actualizarBalance')
]