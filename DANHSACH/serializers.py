from rest_framework import serializers

from .models import Xe, Nhan_vien, Nhan_vien_xe, Capnhat, Tin_nhan, So_dien_thoai_gui, So_dien_thoai_nhan, Muc_nuoc, Thoi_gian, CanhBao

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
        fields = ('id','ngay_tao', 'seri', 'ten_nhan_vien', 'xe')

class CapnhatSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Capnhat
        fields = ('id', 'trang_thai','trang_thai_sdtg', 'trang_thai_sdtn','trang_thai_tn')

class So_dien_thoai_guiSerializer(serializers.ModelSerializer):
   class  Meta:
        model = So_dien_thoai_gui
        fields = ('id', 'sdtg')

class So_dien_thoai_nhanSerializer(serializers.ModelSerializer):
   class  Meta:
        model = So_dien_thoai_nhan
        fields = ('id', 'sdtn')

class Tin_nhanSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Tin_nhan
        fields = ('id', 'ngay_tao','tin_nhan','ma_tn')

class CanhBaoSerializer(serializers.ModelSerializer):
   class  Meta:
        model = CanhBao
        fields = ('id', 'ket_noi_usb','khong_gui_tn')



class Muc_nuocSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Muc_nuoc
        fields = ('id', 'MaTram','Ngay','GiaTri')

class ThoigianSerializer(serializers.ModelSerializer):
   class  Meta:
        model = Thoi_gian
        fields = ('id','ngay_tao', 'trang_thai')