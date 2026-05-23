from django.conf import settings
from django.db import models
from django.db.models import Q


class Campana(models.Model):
    nombre = models.CharField(max_length=200)
    director = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='campanas_dirigidas',
    )
    notas_generales = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_campanas'
        verbose_name = 'campaña'
        verbose_name_plural = 'campañas'

    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='personajes',
    )
    campana = models.ForeignKey(
        Campana,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='personajes',
    )
    nombre = models.CharField(max_length=200)
    experiencia = models.PositiveIntegerField(default=0)
    raza = models.ForeignKey(
        'srd.Raza',
        on_delete=models.PROTECT,
        related_name='personajes',
    )
    fuerza = models.PositiveSmallIntegerField()
    destreza = models.PositiveSmallIntegerField()
    constitucion = models.PositiveSmallIntegerField()
    inteligencia = models.PositiveSmallIntegerField()
    sabiduria = models.PositiveSmallIntegerField()
    carisma = models.PositiveSmallIntegerField()
    puntos_golpe_max = models.PositiveSmallIntegerField()
    puntos_golpe_actuales = models.SmallIntegerField()
    clase_armadura = models.PositiveSmallIntegerField()

    # Tablas puente — accesibles via through models
    clases = models.ManyToManyField(
        'srd.Clase',
        through='PersonajeClase',
        related_name='personajes',
    )

    class Meta:
        db_table = 'user_personajes'
        verbose_name = 'personaje'
        verbose_name_plural = 'personajes'

    def __str__(self):
        return f'{self.nombre} ({self.usuario})'


class PersonajeClase(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    clase = models.ForeignKey('srd.Clase', on_delete=models.PROTECT)
    nivel_en_clase = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'personaje_clases'
        verbose_name = 'clase de personaje'
        verbose_name_plural = 'clases de personaje'
        constraints = [
            models.UniqueConstraint(
                fields=['personaje', 'clase'],
                name='unique_personaje_clase',
            ),
        ]

    def __str__(self):
        return f'{self.personaje} — {self.clase} nv.{self.nivel_en_clase}'


class PersonajeInventario(models.Model):
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        related_name='inventario',
    )
    objeto_srd = models.ForeignKey(
        'srd.Objeto',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+',
    )
    objeto_hb = models.ForeignKey(
        'homebrew.Objeto',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+',
    )
    cantidad = models.PositiveSmallIntegerField(default=1)
    equipado = models.BooleanField(default=False)

    class Meta:
        db_table = 'personaje_inventario'
        verbose_name = 'item de inventario'
        verbose_name_plural = 'inventario'
        constraints = [
            # Exactamente uno de los dos FKs debe estar poblado
            models.CheckConstraint(
                condition=(
                    Q(objeto_srd__isnull=False, objeto_hb__isnull=True)
                    | Q(objeto_srd__isnull=True, objeto_hb__isnull=False)
                ),
                name='inventario_exactamente_un_objeto',
                violation_error_message=(
                    'Un ítem de inventario debe referenciar exactamente un objeto '
                    '(SRD u Homebrew), nunca ambos ni ninguno.'
                ),
            ),
        ]


class PersonajeConjuro(models.Model):
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        related_name='conjuros_conocidos',
    )
    conjuro_srd = models.ForeignKey(
        'srd.Conjuro',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+',
    )
    conjuro_hb = models.ForeignKey(
        'homebrew.Hechizo',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+',
    )
    preparado = models.BooleanField(default=False)

    class Meta:
        db_table = 'personaje_conjuros'
        verbose_name = 'conjuro de personaje'
        verbose_name_plural = 'conjuros de personaje'
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(conjuro_srd__isnull=False, conjuro_hb__isnull=True)
                    | Q(conjuro_srd__isnull=True, conjuro_hb__isnull=False)
                ),
                name='conjuro_exactamente_uno',
                violation_error_message=(
                    'Un conjuro conocido debe referenciar exactamente un hechizo '
                    '(SRD u Homebrew), nunca ambos ni ninguno.'
                ),
            ),
        ]
