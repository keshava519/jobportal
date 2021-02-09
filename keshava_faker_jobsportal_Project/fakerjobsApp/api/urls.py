from django.conf.urls import url,include
from fakerjobsApp.api import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('hydjobsinfo',views.hyd_crud_cbv)
router.register('banglorejobsinfo',views.banglore_crud_cbv)
router.register('chennaijobsinfo',views.chennai_crud_cbv)
router.register('punejobsinfo',views.pune_crud_cbv)

urlpatterns = [
    url(r'',include(router.urls)),
]
