#-*- coding:utf-8 -*-
__author__ = 'uiandwe'

from rest_framework import serializers
from band.models import Band

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band