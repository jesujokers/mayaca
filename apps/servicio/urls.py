from django.urls import path
from apps.servicio.views import index,confirmar,pedir,RegistrarViaje

app_name = 'apps'

urlpatterns = [
	path('', index, name = "index"),
	path('pedir', pedir, name = "pedir"),
	path('confirmar', confirmar, name = "confirmar"),
	path('pedido', RegistrarViaje, name = 'pedido'),
]