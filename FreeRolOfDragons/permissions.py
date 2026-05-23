from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Permite lectura a cualquier request autenticado.
    Escritura solo al propietario del objeto.
    El viewset puede declarar `owner_field` para especificar el campo dueño.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        owner_field = getattr(view, 'owner_field', None)
        if owner_field:
            return getattr(obj, f'{owner_field}_id', None) == request.user.pk
        for field in ('creador_id', 'usuario_id', 'director_id'):
            if hasattr(obj, field):
                return getattr(obj, field) == request.user.pk
        return False
