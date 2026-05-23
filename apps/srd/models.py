from django.db import models


class Raza(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    incremento_atributos = models.JSONField()
    velocidad = models.PositiveIntegerField()
    idiomas = models.JSONField()
    rasgos_raciales = models.JSONField()

    class Meta:
        db_table = 'srd_razas'
        verbose_name = 'raza'
        verbose_name_plural = 'razas'

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    dado_golpe = models.CharField(max_length=10)
    descripcion = models.TextField()

    class Meta:
        db_table = 'srd_clases'
        verbose_name = 'clase'
        verbose_name_plural = 'clases'

    def __str__(self):
        return self.nombre


class Conjuro(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    nivel = models.PositiveSmallIntegerField()
    escuela = models.CharField(max_length=50)
    concentracion = models.BooleanField()
    descripcion = models.TextField()

    class Meta:
        db_table = 'srd_conjuros'
        verbose_name = 'conjuro'
        verbose_name_plural = 'conjuros'

    def __str__(self):
        return self.nombre


class Monstruo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    clase_armadura = models.PositiveSmallIntegerField()
    puntos_golpe = models.PositiveSmallIntegerField()
    fuerza = models.PositiveSmallIntegerField()
    destreza = models.PositiveSmallIntegerField()
    constitucion = models.PositiveSmallIntegerField()
    inteligencia = models.PositiveSmallIntegerField()
    sabiduria = models.PositiveSmallIntegerField()
    carisma = models.PositiveSmallIntegerField()
    desafio = models.CharField(max_length=10)
    acciones = models.JSONField()
    acciones_legendarias = models.JSONField(default=list)

    class Meta:
        db_table = 'srd_monstruos'
        verbose_name = 'monstruo'
        verbose_name_plural = 'monstruos'

    def __str__(self):
        return self.nombre


class Objeto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.CharField(max_length=100)
    rareza = models.CharField(max_length=100)
    es_magico = models.BooleanField()

    class Meta:
        db_table = 'srd_objetos'
        verbose_name = 'objeto'
        verbose_name_plural = 'objetos'

    def __str__(self):
        return self.nombre
