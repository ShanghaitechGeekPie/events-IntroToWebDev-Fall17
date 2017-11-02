from . import models

from rest_framework import serializers


class poiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.poi
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'lat', 
            'lng', 
        )


class snsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.sns
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'api_root', 
        )


class extlnkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.extlnk
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'url', 
        )


class tagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tag
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
        )


