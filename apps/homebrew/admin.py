from django.contrib import admin

from .models import Hechizo, Monstruo, Objeto


@admin.register(Hechizo)
class HechizoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'escuela', 'concentracion', 'creador')
    list_filter = ('nivel', 'escuela', 'concentracion')
    search_fields = ('nombre', 'creador__email')


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'es_magico', 'creador')
    list_filter = ('es_magico',)
    search_fields = ('nombre', 'creador__email')


@admin.register(Monstruo)
class MonstruoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clase_armadura', 'creador')
    search_fields = ('nombre', 'creador__email')
