from django.db import models

# Create your models here.
class Localidad(models.Model):
    nombre = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.nombre