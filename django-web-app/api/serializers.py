from rest_framework import serializers
from .models import DpRequest, DarkPatternsData

class DpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DpRequest
        fields = '__all__'

class DarkPatternsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarkPatternsData
        fields = '__all__'