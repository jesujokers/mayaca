from django.urls import path
from apps.cliente.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = 'index'),
	path('registrar/', RegistrarCliente, name = 'registrar'),
	path('perfil/<int:id_cliente>/', PerfilCliente, name = 'perfil'),
	path('editar/<int:id_cliente>/', EditarCliente, name = 'editar'),
	path('viajes/<int:id_cliente>/', ViajesCliente, name = 'viajes'),
]