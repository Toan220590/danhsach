from django.db import models

# Create your models here.

class Xe(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    ten = models.CharField(max_length = 250)
    bien_so = models.CharField(max_length=250, default="")

class Nhan_vien(models.Model):
    ngay_tao = models.DateTimeField(auto_now_add = True)
    ten = models.CharField(max_length=250)
    xe = models.ForeignKey(Xe, on_delete = models.CASCADE)