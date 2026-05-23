from rest_framework import serializers

from apps.srd.models import Clase, Conjuro, Monstruo, Objeto, Raza


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'


class ConjuroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conjuro
        fields = '__all__'


class MonstruoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monstruo
        fields = '__all__'


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objeto
        fields = '__all__'
