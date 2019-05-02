from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/<nome>', listarClientes),
]