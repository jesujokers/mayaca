from django.urls import path
from apps.chofer.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = 'index'),
	path('registrar/', RegistrarChofer, name = 'registrar'),
	path('editar/<int:id_chofer>/', EditarChofer, name = 'editar'),
]