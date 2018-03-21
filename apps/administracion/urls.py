
from django.urls import path
from apps.administracion.views import *
from django.contrib.auth.decorators import login_required

app_name = 'apps'

urlpatterns = [
	path('', index, name = 'administracion'),
	path('registrar/', RegistrarEmpleado, name = 'registrar'),
	path('listar/', ListarEmpleado, name = 'listar' ),
	path('eliminar/<int:pk>/',UsuarioDelete.as_view(), name = 'eliminar'),
	path('editar/<int:pk>/',UsuarioUpdate.as_view(), name = 'editar'),
	path('suspender/<int:id_usuario>',Suspender, name = 'suspender'),
	path('habilitar/<int:id_usuario>',Habilitar, name = 'habilitar'),
	path('perfil/<int:id_usuario>',PerfilEmpleado, name = 'perfil'),
	path('gestion/', GestionViajes, name = 'gestion'),
	path('panel/',Panel, name = 'panel'),
]