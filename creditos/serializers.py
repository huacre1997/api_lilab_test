from rest_framework import serializers
from creditos.models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def create(self,validated_data):
        user=User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields="__all__"
class SolicitudSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model=Solicitud
        fields="__all__"