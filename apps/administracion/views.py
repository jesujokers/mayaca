from django.shortcuts import render
from apps.administracion.forms import FormUser, FormEmpleado, FormPermisos
from apps.administracion.models import *
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from apps.servicio.models import *
from apps.chofer.models import *
from mayaca.settings import Precio



# Create your views here.

def index(request):
	return render(request, 'administracion/index.html')

class RegistroUsuario(CreateView):
	model = User 
	form_class = FormUser
	template_name = 'administracion/registro.html' 
	success_url = reverse_lazy('administracion/listar')

class UsuarioListar(ListView):
	model = User
	template_name = 'administracion/lista.html'
	paginate_by = 4

class UsuarioDelete(DeleteView):
	model = User 
	template_name = 'administracion/delete.html'
	success_url = reverse_lazy('administracion:listar')

class UsuarioUpdate(UpdateView):
	model = User 
	template_name = 'administracion/registro.html'
	form_class = FormUser
	success_url = reverse_lazy('home:index')

def Suspender(request, id_usuario):
	usuario = User.objects.get(id = id_usuario)
	usuario.is_active = 0
	if request.method == 'POST':
		usuario.save()
		return HttpResponseRedirect(reverse('administracion:listar'))
	return render(request,'administracion/suspender.html', {'usuario':usuario})

def Habilitar(request, id_usuario):
	usuario = User.objects.get(id = id_usuario)
	usuario.is_active = 1
	if request.method == 'POST':
		usuario.save()
		return HttpResponseRedirect(reverse('administracion:listar'))
	return render(request,'administracion/habilitar.html', {'usuario':usuario})



def RegistrarEmpleado(request):
	if request.method == 'POST':
		user_form = FormUser(request.POST)
		empleado_form = FormEmpleado(request.POST, request.FILES)
		permisos_form = FormPermisos(request.POST)
		if empleado_form.is_valid() and user_form.is_valid() and permisos_form.is_valid():
			user = user_form.save()
			user.refresh_from_db()
			permisos = permisos_form.save()

			if permisos.agregar == False or permisos.eliminar == False or permisos.editar == False or permisos.actualizar == False or permisos.suspender == False or permisos.habilitar == False:
				rol = 'Empleado'
			else:
				rol = 'Administrador'

			empleado = Empleado(
				usuario = user, 
				foto = request.FILES['foto'],
				cedula = empleado_form.cleaned_data['cedula'],
				sueldo = empleado_form.cleaned_data['sueldo'],
				fecha_nacimiento = empleado_form.cleaned_data['fecha_nacimiento'],
				direccion = empleado_form.cleaned_data['direccion'],
				telefono = empleado_form.cleaned_data['telefono'],
				rol = rol,
				permisos = permisos
				)
			empleado.save()
			bitacora = BitacoraEmpleado(
				user = request.user,
				descripcion = "Registro"
				)
			bitacora.save()
			if request.user.is_authenticated:
				return HttpResponseRedirect(reverse('administracion:listar'))
			login(request, user)
			return HttpResponseRedirect(reverse('home:index'))
	else:
		user_form = FormUser
		empleado_form = FormEmpleado
		permisos_form = FormPermisos
	return render(request, 'administracion/registro.html',{
       	'user_form': user_form,
       	'empleado_form': empleado_form,
       	'permisos_form': permisos_form
       	})

def EditarEmpleado(request,id_empleado):
	if request.user.is_authenticated:
		editar = True
		empleado = User.objects.get(id = id_empleado)
		if request.method == 'GET':
			empleado_form = FormEmpleado(instance = empleado.empleado)
			user_form = FormUser(instance = empleado)
			permisos_form = FormPermisos(instance = empleado.empleado.permisos)
		else:
			empleado_form = FormEmpleado(request.POST, instance = empleado.empleado)
			user_form = FormUser(request.POST, instance = empleado)
			if empleado_form.is_valid() and user_form.is_valid():
				usuario = user_form.save()
				empleado_form.save()
				bitacora = BitacoraEmpleado(
					user = request.user,
					descripcion = "Edicion"
					)
				bitacora.save()
				login(request, usuario)
				return HttpResponseRedirect(reverse('home:index'))
	return render(request, 'administracion/registro.html',{
		'empleado_form': empleado_form,
		'user_form': user_form,
		'permisos_form': permisos_form,
		'editar': editar
		})


def ListarEmpleado(request):
	if request.user.is_authenticated:
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True: 
			empleados = Empleado.objects.all()
			contexto = {'empleados': empleados}
			return render(request, 'administracion/lista.html', contexto)
	return render(request, 'administracion/lista.html')

def PerfilEmpleado(request, id_empleado):
	if request.user.is_authenticated:
		empleado = Empleado.objects.filter(usuario = request.user.id)
		if empleado.exists() == True:
			usuario_actual = request.user.id 
			empleado = Empleado.objects.filter(usuario = usuario_actual)
			if empleado.exists() == True:
				empleado = Empleado.objects.filter(id = id_empleado)
				if empleado.exists == True:
					empleado = Empleado.objects.get(id = id_empleado)
					return render(request, 'administracion/perfil.html', {'empleado':empleado})
	return render(request, 'administracion/perfil.html')

def Panel(request):
	if request.user.is_authenticated:
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True:
			panel = True
			bandera_chofer = False
			choferes = Chofer.objects.all()
			for chofer in choferes:
				if chofer.usuario.is_active == False:
					bandera_chofer = True
			return render(request, 'administracion/panel.html',{'bandera_chofer':bandera_chofer, 'panel':panel})	
	return render(request, 'administracion/panel.html')

def CambiarPrecio(request,precio_nuevo):
	Precio = precio_nuevo
	return HttpResponseRedirect(reverse('home:index'))