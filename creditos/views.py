from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from creditos.models import *
from django.contrib.auth.models import User
from creditos.serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(["GET","POST"])
def usuario_api_view(request):
    if request.method=="GET":
        usuarios=User.objects.all()
        usuarios_serializer=UserSerializer(usuarios,many=True)
        return Response(usuarios_serializer.data,status=status.HTTP_200_OK)
    if request.method=="POST":
        usuario_serializer=UserSerializer(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

@api_view(["GET","POST"])
def cliente_api_view(request):
    if request.method=="GET":
        clientes=Cliente.objects.all()
        clientes_serializer=ClienteSerializer(clientes,many=True)
        return Response(clientes_serializer.data,status=status.HTTP_200_OK)
    if request.method=="POST":
        cliente_serializer=ClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(clientes_serializer.errors)
@api_view(["GET","POST"])
def solicitud_api_view(request):
    if request.method=="GET":
        solicitudes=Solicitud.objects.all()
        solicitudes_serializer=SolicitudSerializer(solicitudes,many=True)
        return Response(solicitudes_serializer.data,status=status.HTTP_200_OK)    
    if request.method=="POST":
        solicitud_serializer=SolicitudSerializer(data=request.data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return Response(solicitud_serializer.data)
        return Response(solicitud_serializer.errors)
@api_view(["GET","PUT"])
def solicitud_detalle_api_view(request,pk=None):
    queryset=Solicitud.objects.filter(id=pk)
    if queryset.exists():
        solicitud=queryset.get()
        if request.method=="GET":
            solicitud_serializer=SolicitudSerializer(solicitud)
            return Response(solicitud_serializer.data,status=status.HTTP_200_OK)
        elif request.method=="PUT":
            solicitud_serializer=SolicitudSerializer(solicitud,data=request.data)
            if solicitud_serializer.is_valid():
                solicitud_serializer.save()
                return Response(solicitud_serializer.data,status=status.HTTP_200_OK)
            return Response(solicitud_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({"mensaje":"La solicitud no existe."},status=status.HTTP_400_BAD_REQUEST)