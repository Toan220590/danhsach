from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from.views import XeViewSet, Nhan_vienViewSet, Nhan_vien_xeViewSet, CapnhatViewSet, So_dien_thoai_guiViewSet, So_dien_thoai_nhanViewSet, Tin_nhanViewSet

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('xe', XeViewSet)
router.register('nhanvien', Nhan_vienViewSet)
router.register('nhanvienxe', Nhan_vien_xeViewSet)
router.register('capnhat', CapnhatViewSet)
router.register('sdtg', So_dien_thoai_guiViewSet)
router.register('sdtn', So_dien_thoai_nhanViewSet)
router.register('tn', Tin_nhanViewSet)

urlpatterns = [
    path('', include(router.urls)),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]