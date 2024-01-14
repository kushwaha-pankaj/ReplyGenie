from rest_framework import serializers
from .models import CustomerQuery

class CustomerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuery
        fields = '__all__'
