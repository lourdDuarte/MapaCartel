from django.forms import ModelForm
  
from django import forms
from django.core.exceptions import ValidationError
from .models import Cartel

class CartelForm(ModelForm):
    
    class Meta:
        model = Cartel
        fields = '__all__'
        
        required = ['usuario','domicilio','nombre', 'localidad', 'latitud', 'longitud', 'imagen_cartel', 'proveedor', 'medidas', 'altura', 'largo', 'metros_cuadrados']
        
        
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
       
  
        # Realizar la validación para asegurarse de que no haya comas
        if ',' in latitud:
            raise forms.ValidationError("La latitud no debe contener comas.")
        
        
        return latitud
    
    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
  
        # Realizar la validación para asegurarse de que no haya comas
        if ',' in longitud:
            raise forms.ValidationError("La longitud no debe contener comas.")
        
        return longitud
    
    

    