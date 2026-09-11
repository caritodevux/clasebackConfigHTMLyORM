from django.contrib import admin

# Register your models here.
from .models import Libro

# admin.site.register(Libro)
#Creamos una configuración personalizada para mostrar nuestro models en el admin
class LibroAdmin(admin.ModelAdmin):
    #Definimos las columnas que queremos ver en el listado
    'id',
    'titulo',
    'autor',
    'categoria',
    'categorias_publicacion',
    'disponible',

    #activamos un buscador de libros
    search_fields = ('titulo','autor',)

    #activamos un filtro de registros
    list_filter = ('categoria','disponible',)

#Registramos la clase Model para el admin
admin.site.register(Libro, LibroAdmin) 