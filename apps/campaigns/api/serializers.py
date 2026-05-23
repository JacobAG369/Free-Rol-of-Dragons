from rest_framework import serializers

from apps.campaigns.models import (
    Campana,
    Personaje,
    PersonajeClase,
    PersonajeConjuro,
    PersonajeInventario,
)


class CampanaSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Campana
        fields = '__all__'
        read_only_fields = ('director', 'fecha_creacion')


class PersonajeClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonajeClase
        fields = ('id', 'clase', 'nivel_en_clase')


class PersonajeInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonajeInventario
        fields = ('id', 'objeto_srd', 'objeto_hb', 'cantidad', 'equipado')

    def validate(self, data):
        objeto_srd = data.get('objeto_srd')
        objeto_hb = data.get('objeto_hb')
        if bool(objeto_srd) == bool(objeto_hb):
            raise serializers.ValidationError(
                'Especifica exactamente un objeto: SRD u Homebrew, no ambos ni ninguno.'
            )
        return data


class PersonajeConjuroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonajeConjuro
        fields = ('id', 'conjuro_srd', 'conjuro_hb', 'preparado')

    def validate(self, data):
        conjuro_srd = data.get('conjuro_srd')
        conjuro_hb = data.get('conjuro_hb')
        if bool(conjuro_srd) == bool(conjuro_hb):
            raise serializers.ValidationError(
                'Especifica exactamente un conjuro: SRD u Homebrew, no ambos ni ninguno.'
            )
        return data


class PersonajeSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    clases = PersonajeClaseSerializer(
        source='personajeclase_set', many=True, read_only=True
    )
    inventario = PersonajeInventarioSerializer(many=True, read_only=True)
    conjuros_conocidos = PersonajeConjuroSerializer(many=True, read_only=True)

    class Meta:
        model = Personaje
        fields = '__all__'
        read_only_fields = ('usuario',)
