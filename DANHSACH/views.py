from django.shortcuts import render
from rest_framework import viewsets

from .models import Xe, Nhan_vien
from .serializers import XeSerializer, Nhan_vienSerializer

# Create your views here.

class XeViewSet(viewsets.ModelViewSet):
    queryset = Xe.objects.all()
    serializer_class = XeSerializer

class Nhan_vienViewSet(viewsets.ModelViewSet):
    queryset = Nhan_vien.objects.all()
    serializer_class = Nhan_vienSerializer