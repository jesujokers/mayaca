from django.conf.urls import include
from django.urls import path
from apps.home.views import *

app_name = 'apps'

urlpatterns = [
	path('', index, name = "index"),
]