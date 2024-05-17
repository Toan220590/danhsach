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
    trang_thai = models.BooleanField(default=False)

class So_dien_thoai_gui(models.Model):
    sdtg = models.CharField(max_length=250)

class So_dien_thoai_nhan(models.Model):
    sdtn = models.CharField(max_length=250)

class Tin_nhan(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    tin_nhan = models.CharField(max_length=1000)