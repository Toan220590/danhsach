from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


from .models import Xe, Nhan_vien, Nhan_vien_xe
from .serializers import XeSerializer, Nhan_vienSerializer, Nhan_vien_xeSerializer

# Create your views here.

class XeViewSet(viewsets.ModelViewSet):
    queryset = Xe.objects.all()
    serializer_class = XeSerializer


class Nhan_vienViewSet(viewsets.ModelViewSet):
    queryset = Nhan_vien.objects.all()
    serializer_class = Nhan_vienSerializer

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        filtered_data = Nhan_vien.objects.filter(xe=pk)
        serializer = Nhan_vienSerializer(filtered_data, many=True)
        return Response(serializer.data)

class Nhan_vien_xeViewSet(viewsets.ModelViewSet):
    queryset = Nhan_vien_xe.objects.all()
    serializer_class = Nhan_vien_xeSerializer