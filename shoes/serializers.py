from rest_framework import serializers

from shoes.models import Manufacturer, ShoeColor, ShoeType, Shoe

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website'
        ]


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color'
        ]

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = [
            'style'
        ]

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'material',
            'fasten_type',
            'manufacturer',
            'color',
            'shoe_type'
        ]