from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250, blank=False, null=False )
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    icono = models.FileField(upload_to='iconos/', null=True, blank=True)



    def __str__(self) :
        return self.nombre