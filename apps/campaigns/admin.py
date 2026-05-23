from django.contrib import admin

from .models import (
    Campana,
    Personaje,
    PersonajeClase,
    PersonajeConjuro,
    PersonajeInventario,
)


class PersonajeClaseInline(admin.TabularInline):
    model = PersonajeClase
    extra = 1


class PersonajeInventarioInline(admin.TabularInline):
    model = PersonajeInventario
    extra = 0


class PersonajeConjuroInline(admin.TabularInline):
    model = PersonajeConjuro
    extra = 0


@admin.register(Campana)
class CampanaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'director', 'fecha_creacion')
    search_fields = ('nombre', 'director__email')


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'campana', 'raza', 'experiencia')
    list_filter = ('campana', 'raza')
    search_fields = ('nombre', 'usuario__email')
    inlines = [PersonajeClaseInline, PersonajeInventarioInline, PersonajeConjuroInline]
