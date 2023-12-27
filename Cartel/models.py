from django.db import models
from Localidad.models import Localidad
from django.contrib.auth.models import User
from proveedor.models import Proveedor
from precioProveedor.models import PrecioProveedor
# Create your models here.
class Cartel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=200, blank=False, null=False)
    longitud = models.CharField(max_length=200, blank=False, null=False)
    direccion = models.CharField(max_length=250, blank=False, null=False)
    imagen_cartel = models.FileField(upload_to='carteles/')
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    altura = models.CharField(max_length=250, blank=False, null=False)
    largo = models.CharField(max_length=250, blank=False, null=False)
    metros_cuadrados = models.CharField(max_length=250, blank=False, null=True)
    metros_cuadrados_precio = models.CharField(max_length=250, blank=True, null=True)
    
    

    
    def __str__(self):
        return self.nombre