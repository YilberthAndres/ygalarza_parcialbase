from django.contrib import admin
from apps.mantenimientos.models import Mantenimiento
# Register your models here.
class MantenimientosAdmin(admin.ModelAdmin):
    list_display  = ('fecha', 'solicitud', 'tiempo_atencion');
    ordering      = ('fecha', 'solicitud', 'tiempo_atencion');
    search_fields = ('fecha', 'solicitud');


admin.site.register(Mantenimiento, MantenimientosAdmin);