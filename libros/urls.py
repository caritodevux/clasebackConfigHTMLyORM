from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_libros, name = 'listar_libros')
]