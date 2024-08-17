from rest_framework import serializers
from .models import TitanicPassenger

class TitanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitanicPassenger
        fields = '__all__'