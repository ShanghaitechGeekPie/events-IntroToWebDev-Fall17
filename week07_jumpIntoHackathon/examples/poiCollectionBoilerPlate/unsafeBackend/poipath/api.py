from . import models
from . import serializers
from rest_framework import viewsets, permissions


class poiViewSet(viewsets.ModelViewSet):
    """ViewSet for the poi class"""

    queryset = models.poi.objects.all()
    serializer_class = serializers.poiSerializer
    permission_classes = [permissions.AllowAny]


class snsViewSet(viewsets.ModelViewSet):
    """ViewSet for the sns class"""

    queryset = models.sns.objects.all()
    serializer_class = serializers.snsSerializer
    permission_classes = [permissions.AllowAny]


class extlnkViewSet(viewsets.ModelViewSet):
    """ViewSet for the extlnk class"""

    queryset = models.extlnk.objects.all()
    serializer_class = serializers.extlnkSerializer
    permission_classes = [permissions.AllowAny]


class tagViewSet(viewsets.ModelViewSet):
    """ViewSet for the tag class"""

    queryset = models.tag.objects.all()
    serializer_class = serializers.tagSerializer
    permission_classes = [permissions.AllowAny]


