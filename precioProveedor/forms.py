from django.forms import ModelForm
  
from django import forms
from django.core.exceptions import ValidationError
from .models import PrecioProveedor


class PrecioProveedorForm(ModelForm):
    model = PrecioProveedor
    fields = '__all__'
        
    required = ['descripcio','precio']