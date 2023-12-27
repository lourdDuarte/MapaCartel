from django.db import models
from proveedor.models import Proveedor

# Create your models here.
class PrecioProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250, blank=False, null=False)
    precio = models.CharField(max_length=250, blank=False, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.descripcion + "-" + self.precio