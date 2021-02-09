from rest_framework import serializers
from fakerjobsApp.models import *


class HydjobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hydjobs
        fields='__all__'

class BanglorejobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banglorejobs
        fields='__all__'

class ChennaijobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chennaijobs
        fields='__all__'

class PunejobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Punejobs
        fields='__all__'
