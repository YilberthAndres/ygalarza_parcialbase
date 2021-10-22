from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    fecha           = models.DateField(verbose_name="Fecha")
    solicitud       = models.IntegerField(verbose_name="Solicitud");
    tiempo_atencion = models.DurationField(verbose_name="Tiempo_Atencion")


    def _str__(self):
        return self.solicitud;
    
    class Meta:
        verbose_name        = "Mantenimiento"
        verbose_name_plural = "Mantenimientos"