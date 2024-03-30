from rest_framework import serializers

from .models import Xe, Nhan_vien

class XeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xe
        fields = ('id','time', 'ten')

class Nhan_vienSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Nhan_vien
        fields = ('id','ngay_tao', 'ten', 'xe')