from rest_framework import serializers

from apps.homebrew.models import Hechizo, Monstruo, Objeto


class HechizoSerializer(serializers.ModelSerializer):
    creador = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Hechizo
        fields = '__all__'
        read_only_fields = ('creador',)


class ObjetoSerializer(serializers.ModelSerializer):
    creador = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Objeto
        fields = '__all__'
        read_only_fields = ('creador',)


class MonstruoSerializer(serializers.ModelSerializer):
    creador = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Monstruo
        fields = '__all__'
        read_only_fields = ('creador',)
