from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm 

# Create your views here.
def listar_libros(request):
    # Utilizamos Django ORM para obtener todos los libros alamcenados
    libros = Libro.objects.all()
    #render recibe 3 cosas: request, template a cargar, datos a utilizar
    return render(
        request, 
        'libros/listar_libros.html',
        {'libros'= libros}
    )