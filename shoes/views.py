from django.shortcuts import render
from rest_framework import viewsets

from shoes.models import Manufacturer, ShoeColor, ShoeType, Shoe
from shoes.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer

# Create your views here.
class ManufacturerViewSet(viewsets.ViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeColorViewSet(viewsets.ViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeViewSet(viewsets.ViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer