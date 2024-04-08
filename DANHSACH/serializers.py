from rest_framework import serializers

from .models import Xe, Nhan_vien, Nhan_vien_xe, Cap_nhat

class XeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xe
        fields = ('id','ngay_tao', 'ten_xe','bien_so')

class Nhan_vienSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Nhan_vien
        fields = ('ngay_tao', 'seri', 'ten_nhan_vien', 'nam_sinh', 'cccd', 'xe')

class Nhan_vien_xeSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Nhan_vien_xe
        fields = ('ngay_tao', 'seri', 'ten_nhan_vien', 'xe')

class Cap_nhatSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Cap_nhat
        fields = ('id', 'trang_thai')