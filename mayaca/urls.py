"""mayaca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples: 
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/', include('apps.home.urls', namespace = 'home')),
    path('cliente/', include('apps.cliente.urls',namespace = 'cliente')),
    path('administracion/', include('apps.administracion.urls', namespace = 'administracion')),
    path('chofer/', include('apps.chofer.urls', namespace = 'chofer')),
    path('servicio/', include('apps.servicio.urls', namespace = 'servicio')),
    path('accounts/', include ('django.contrib.auth.urls')),
]