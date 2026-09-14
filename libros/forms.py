#Generar formularios automaticos para un models
from django import forms
from .models import Libro

# ModelForm permite crear automaticamente un formulario utilizando un models
class LibroForm(forms.ModelForm):
    #Metaclase
    class Meta:
        #a que modelo estamos apuntando
        model = Libro
        #indicamos que campos queremos ver en pantalla
        fields = [
            'titulo',
            'autor',
            'categoria',
            'anio_publicacion',
            'disponible',
        ] 