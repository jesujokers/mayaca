from django.urls import path
from apps.servicio.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = "index"),
	path('pedir', pedir, name = "pedir"),
	path('confirmar', confirmar, name = "confirmar"),
	path('pedido', RegistrarViaje, name = 'pedido'),
	path('gestion/', GestionViajes, name = 'gestion'),
	path('detalles/<int:id_viaje>', DetallesViaje, name = 'detalles'),
	path('cancelar/<int:id_viaje>', CancelarViaje, name = 'cancelar'),
	path('despachar/<int:id_viaje>', DespacharViaje, name = 'despachar'),
]