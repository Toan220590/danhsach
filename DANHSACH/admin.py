from django.contrib import admin

from . models import Xe, Nhan_vien,Nhan_vien_xe, Cap_nhat

# Register your models here.

admin.site.register(Xe)
admin.site.register(Nhan_vien)
admin.site.register(Nhan_vien_xe)
admin.site.register(Cap_nhat)
