from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.srd.models import Clase, Conjuro, Monstruo, Objeto, Raza

from .serializers import (
    ClaseSerializer,
    ConjuroSerializer,
    MonstruoSerializer,
    ObjetoSerializer,
    RazaSerializer,
)


class RazaViewSet(ReadOnlyModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClaseViewSet(ReadOnlyModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ConjuroViewSet(ReadOnlyModelViewSet):
    queryset = Conjuro.objects.all()
    serializer_class = ConjuroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['nivel', 'escuela', 'concentracion']


class MonstruoViewSet(ReadOnlyModelViewSet):
    queryset = Monstruo.objects.all()
    serializer_class = MonstruoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['desafio']


class ObjetoViewSet(ReadOnlyModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['es_magico', 'rareza']
