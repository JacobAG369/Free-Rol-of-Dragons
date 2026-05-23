from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.homebrew.models import Hechizo, Monstruo, Objeto
from FreeRolOfDragons.permissions import IsOwnerOrReadOnly

from .serializers import HechizoSerializer, MonstruoSerializer, ObjetoSerializer


class _HomebrewViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    owner_field = 'creador'

    def perform_create(self, serializer):
        serializer.save(creador=self.request.user)


class HechizoViewSet(_HomebrewViewSet):
    queryset = Hechizo.objects.select_related('creador').all()
    serializer_class = HechizoSerializer


class ObjetoViewSet(_HomebrewViewSet):
    queryset = Objeto.objects.select_related('creador').all()
    serializer_class = ObjetoSerializer


class MonstruoViewSet(_HomebrewViewSet):
    queryset = Monstruo.objects.select_related('creador').all()
    serializer_class = MonstruoSerializer
