from rest_framework import serializers
from .models import DpRequest

class DpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DpRequest
        fields = '__all__'


