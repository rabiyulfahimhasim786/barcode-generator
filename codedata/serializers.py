from rest_framework import serializers
from .models import Barcodefile, Barcode

class Barcodefileserializers(serializers.ModelSerializer):
    class Meta:
        model = Barcodefile
        fields = '__all__'

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['id', 'number', 'pdf']