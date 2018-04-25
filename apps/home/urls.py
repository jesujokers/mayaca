from django.conf.urls import include
from django.urls import path
from apps.home.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = "index"),
	path('acerca_de/', acerca_de, name = "acerca_de"),
	path('terminos-y-condiciones/', terminos, name = "terminos"),
]