from django.urls import path
from apps.chofer.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = 'index'),
	path('registrar/', RegistrarChofer, name = 'registrar'),
	path('editar/<int:id_chofer>/', EditarChofer, name = 'editar'),
	path('perfil/<int:id_chofer>/', PerfilChofer, name = 'perfil'),
	path('listar/',ListarChofer, name = 'listar'),
	path('trabajar/<int:id_chofer>/', Trabajar, name = 'trabajar'),
	path('gestion/',Gestion, name = 'gestion'),
]