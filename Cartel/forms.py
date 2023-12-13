from django.forms import ModelForm
  
from django import forms
from django.core.exceptions import ValidationError
from .models import Cartel

class CartelForm(ModelForm):
    
    class Meta:
        model = Cartel
        fields = '__all__'
        
        required = ['usuario','domicilio','nombre', 'localidad', 'latitud', 'longitud', 'imagen_cartel', 'proveedor', 'medidas']
        
        
