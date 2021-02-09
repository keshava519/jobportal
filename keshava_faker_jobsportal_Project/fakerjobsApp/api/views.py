from rest_framework import viewsets
from fakerjobsApp.models import *
from fakerjobsApp.api.serializers import *


class hyd_crud_cbv(viewsets.ModelViewSet):
    queryset=Hydjobs.objects.all()
    serializer_class=HydjobsSerializer

class banglore_crud_cbv(viewsets.ModelViewSet):
    queryset=Banglorejobs.objects.all()
    serializer_class=BanglorejobsSerializer

class chennai_crud_cbv(viewsets.ModelViewSet):
    queryset=Chennaijobs.objects.all()
    serializer_class=ChennaijobsSerializer

class pune_crud_cbv(viewsets.ModelViewSet):
    queryset=Punejobs.objects.all()
    serializer_class=PunejobsSerializer
