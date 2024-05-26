from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


from .models import Xe, Nhan_vien, Nhan_vien_xe, Capnhat, So_dien_thoai_gui, So_dien_thoai_nhan, Tin_nhan, Muc_nuoc,Thoi_gian
from .serializers import XeSerializer, Nhan_vienSerializer, Nhan_vien_xeSerializer, CapnhatSerializer, So_dien_thoai_guiSerializer, So_dien_thoai_nhanSerializer, Tin_nhanSerializer, Muc_nuocSerializer,ThoigianSerializer

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

class CapnhatViewSet(viewsets.ModelViewSet):
    queryset = Capnhat.objects.all()
    serializer_class = CapnhatSerializer

class So_dien_thoai_guiViewSet(viewsets.ModelViewSet):
    queryset = So_dien_thoai_gui.objects.all()
    serializer_class = So_dien_thoai_guiSerializer

class So_dien_thoai_nhanViewSet(viewsets.ModelViewSet):
    queryset = So_dien_thoai_nhan.objects.all()
    serializer_class = So_dien_thoai_nhanSerializer

class Tin_nhanViewSet(viewsets.ModelViewSet):
    queryset = Tin_nhan.objects.all()
    serializer_class = Tin_nhanSerializer

class Muc_nuocViewSet(viewsets.ModelViewSet):
    queryset = Muc_nuoc.objects.all()
    serializer_class = Muc_nuocSerializer

class ThoigianViewSet(viewsets.ModelViewSet):
    queryset = Thoi_gian.objects.all()
    serializer_class = ThoigianSerializer
