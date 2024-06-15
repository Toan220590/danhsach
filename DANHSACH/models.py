from django.db import models

# Create your models here.

class Xe(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    ten_xe = models.CharField(max_length=250)
    bien_so = models.CharField(max_length=250, default="")

class Nhan_vien(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    seri = models.CharField(max_length=250,primary_key=True)
    ten_nhan_vien = models.CharField(max_length=250)
    nam_sinh = models.CharField(max_length=250)
    cccd = models.CharField(max_length=250)
    xe = models.ForeignKey(Xe, on_delete = models.CASCADE)

class Nhan_vien_xe(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    seri = models.CharField(max_length=250)
    ten_nhan_vien = models.CharField(max_length=250)
    xe = models.ForeignKey(Xe, on_delete = models.CASCADE)

class Capnhat(models.Model):
    trang_thai = models.BooleanField(default=True)
    trang_thai_sdtg = models.BooleanField(default=False)
    trang_thai_sdtn = models.BooleanField(default=False)
    trang_thai_tn = models.BooleanField(default=False)

class CanhBao(models.Model):
    ket_noi_usb= models.BooleanField(default=False)
    khong_gui_tn = models.BooleanField(default=False)


class So_dien_thoai_gui(models.Model):
    sdtg = models.CharField(max_length=250)

class So_dien_thoai_nhan(models.Model):
    sdtn = models.CharField(max_length=250)
    trang_thai_nhan_tn = models.BooleanField(default=False)
    loi_sim = models.BooleanField(default=False)

class Tin_nhan(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    ma_tn= models.CharField(max_length=1000)
    tin_nhan = models.CharField(max_length=1000)

class Muc_nuoc(models.Model):
    MaTram=models.IntegerField(default=0)
    Ngay = models.CharField(max_length=255)
    GiaTri = models.FloatField(default = 0)

class Thoi_gian(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    trang_thai = models.BooleanField(default=False)