from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class _HomebrewBase(models.Model):
    """Campos y validación comunes a todo contenido homebrew."""

    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
    )

    def clean(self):
        if not self.creador_id:
            raise ValidationError({'creador': 'Todo contenido homebrew debe tener un creador.'})

    class Meta:
        abstract = True


class Hechizo(_HomebrewBase):
    nombre = models.CharField(max_length=200)
    nivel = models.PositiveSmallIntegerField()
    escuela = models.CharField(max_length=50)
    concentracion = models.BooleanField()

    class Meta:
        db_table = 'homebrew_hechizos'
        verbose_name = 'hechizo homebrew'
        verbose_name_plural = 'hechizos homebrew'
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'creador'], name='unique_hechizo_por_creador'),
        ]

    def __str__(self):
        return f'{self.nombre} ({self.creador})'


class Objeto(_HomebrewBase):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    es_magico = models.BooleanField()

    class Meta:
        db_table = 'homebrew_objetos'
        verbose_name = 'objeto homebrew'
        verbose_name_plural = 'objetos homebrew'
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'creador'], name='unique_objeto_por_creador'),
        ]

    def __str__(self):
        return f'{self.nombre} ({self.creador})'


class Monstruo(_HomebrewBase):
    nombre = models.CharField(max_length=200)
    clase_armadura = models.PositiveSmallIntegerField()
    acciones = models.JSONField()

    class Meta:
        db_table = 'homebrew_monstruos'
        verbose_name = 'monstruo homebrew'
        verbose_name_plural = 'monstruos homebrew'
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'creador'], name='unique_monstruo_por_creador'),
        ]

    def __str__(self):
        return f'{self.nombre} ({self.creador})'
