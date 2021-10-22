from django.db import models
from apps.mantenimientos.models import Mantenimiento
# Create your models here.
class Equipo(models.Model):
    nombre        = models.CharField(max_length=50, verbose_name="Nombre");
    marca         = models.CharField(max_length=50, verbose_name="Marca");
    modelo        = models.CharField(max_length=50, verbose_name="Modelo");
    mantenimiento = models.ManyToManyField(Mantenimiento, through="Mantenimiento_Equipos");


    def _str__(self):
        return self.nombre;
    
    class Meta:
        verbose_name        = "Equipo"
        verbose_name_plural = "Equipos"


class Mantenimiento_Equipos(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE,verbose_name="Mantenimiento");
    Equipo        = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name="Equipo");
    descripcion   = models.CharField(max_length=50, verbose_name="Descripcion");
    resultado     = models.BooleanField(verbose_name="Resultado")