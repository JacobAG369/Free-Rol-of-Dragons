from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.campaigns.api.views import (
    CampanaViewSet,
    PersonajeClaseViewSet,
    PersonajeConjuroViewSet,
    PersonajeInventarioViewSet,
    PersonajeViewSet,
)
from apps.homebrew.api.views import (
    HechizoViewSet,
    MonstruoViewSet as HomebrewMonstruoViewSet,
    ObjetoViewSet as HomebrewObjetoViewSet,
)
from apps.srd.api.views import (
    ClaseViewSet,
    ConjuroViewSet,
    MonstruoViewSet,
    ObjetoViewSet,
    RazaViewSet,
)

router = DefaultRouter()

# SRD — solo lectura
router.register('srd/razas', RazaViewSet, basename='raza')
router.register('srd/clases', ClaseViewSet, basename='clase')
router.register('srd/conjuros', ConjuroViewSet, basename='conjuro')
router.register('srd/monstruos', MonstruoViewSet, basename='monstruo')
router.register('srd/objetos', ObjetoViewSet, basename='objeto')

# Homebrew — CRUD con ownership
router.register('homebrew/hechizos', HechizoViewSet, basename='hb-hechizo')
router.register('homebrew/objetos', HomebrewObjetoViewSet, basename='hb-objeto')
router.register('homebrew/monstruos', HomebrewMonstruoViewSet, basename='hb-monstruo')

# Campañas — CRUD propio del usuario
router.register('campanas', CampanaViewSet, basename='campana')
router.register('personajes', PersonajeViewSet, basename='personaje')
router.register('personajes-clases', PersonajeClaseViewSet, basename='personaje-clase')
router.register('personajes-inventario', PersonajeInventarioViewSet, basename='personaje-inventario')
router.register('personajes-conjuros', PersonajeConjuroViewSet, basename='personaje-conjuro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.users.api.urls')),
    path('api/v1/', include(router.urls)),
]
