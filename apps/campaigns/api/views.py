from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.campaigns.models import (
    Campana,
    Personaje,
    PersonajeClase,
    PersonajeConjuro,
    PersonajeInventario,
)
from FreeRolOfDragons.permissions import IsOwnerOrReadOnly

from .serializers import (
    CampanaSerializer,
    PersonajeClaseSerializer,
    PersonajeConjuroSerializer,
    PersonajeInventarioSerializer,
    PersonajeSerializer,
)


class CampanaViewSet(ModelViewSet):
    serializer_class = CampanaSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    owner_field = 'director'

    def get_queryset(self):
        return Campana.objects.filter(director=self.request.user).select_related('director')

    def perform_create(self, serializer):
        serializer.save(director=self.request.user)


class PersonajeViewSet(ModelViewSet):
    serializer_class = PersonajeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    owner_field = 'usuario'

    def get_queryset(self):
        return (
            Personaje.objects
            .filter(usuario=self.request.user)
            .select_related('usuario', 'campana', 'raza')
            .prefetch_related(
                'personajeclase_set__clase',
                'inventario',
                'conjuros_conocidos',
            )
        )

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PersonajeClaseViewSet(ModelViewSet):
    serializer_class = PersonajeClaseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return PersonajeClase.objects.filter(personaje__usuario=self.request.user)

    def has_object_permission(self, request, view, obj):
        return obj.personaje.usuario == request.user


class PersonajeInventarioViewSet(ModelViewSet):
    serializer_class = PersonajeInventarioSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return PersonajeInventario.objects.filter(personaje__usuario=self.request.user)

    def has_object_permission(self, request, view, obj):
        return obj.personaje.usuario == request.user


class PersonajeConjuroViewSet(ModelViewSet):
    serializer_class = PersonajeConjuroSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return PersonajeConjuro.objects.filter(personaje__usuario=self.request.user)

    def has_object_permission(self, request, view, obj):
        return obj.personaje.usuario == request.user
