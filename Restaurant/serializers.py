from rest_framework import serializers
from .models import Menu, Reservas


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ReservasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'
