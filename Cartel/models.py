from django.db import models
from Localidad.models import Localidad
from django.contrib.auth.models import User
from proveedor.models import Proveedor
# Create your models here.
class Cartel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    latitud = models.CharField(max_length=200, blank=False, null=False)
    longitud = models.CharField(max_length=200, blank=False, null=False)
    direccion = models.CharField(max_length=250, blank=False, null=False)
    medidas = models.CharField(max_length=250, blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen_cartel = models.FileField(upload_to='carteles/')

    def __str__(self):
        return self.nombre