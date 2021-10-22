from django.contrib import admin
from apps.equipos.models import Equipo, Mantenimiento_Equipos
# Register your models here.

class MembershipInline(admin.TabularInline):
    '''Tabular Inline View for'''

    model = Mantenimiento_Equipos
    extra = 1

class EquiposAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display  = ('nombre', 'marca', 'modelo');
    ordering      = ('nombre', 'marca', 'modelo');
    search_fields = ('nombre', 'marca', 'modelo');


admin.site.register(Equipo, EquiposAdmin);