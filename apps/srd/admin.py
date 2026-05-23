from django.contrib import admin
from .models import Raza, Clase, Conjuro, Monstruo, Objeto


@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'velocidad')
    search_fields = ('nombre',)


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dado_golpe')
    search_fields = ('nombre',)


@admin.register(Conjuro)
class ConjuroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'escuela', 'concentracion')
    list_filter = ('nivel', 'escuela', 'concentracion')
    search_fields = ('nombre',)


@admin.register(Monstruo)
class MonstruoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clase_armadura', 'puntos_golpe', 'desafio')
    list_filter = ('desafio',)
    search_fields = ('nombre',)


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'rareza', 'es_magico')
    list_filter = ('es_magico', 'rareza')
    search_fields = ('nombre',)
