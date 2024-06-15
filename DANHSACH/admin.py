from django.contrib import admin

from . models import Xe, Nhan_vien,Nhan_vien_xe, Capnhat, So_dien_thoai_gui, So_dien_thoai_nhan, Tin_nhan, Muc_nuoc, Thoi_gian, CanhBao

# Register your models here.

admin.site.register(Xe)
admin.site.register(Nhan_vien)
admin.site.register(Nhan_vien_xe)
admin.site.register(Capnhat)
admin.site.register(So_dien_thoai_gui)
admin.site.register(So_dien_thoai_nhan)
admin.site.register(Tin_nhan)
admin.site.register(Muc_nuoc)
admin.site.register(Thoi_gian)
admin.site.register(CanhBao)