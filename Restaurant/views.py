from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializers, ReservasSerializers
from .models import Menu, Reservas


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializers


def index(request):
    return render(request, 'index.html', {})


