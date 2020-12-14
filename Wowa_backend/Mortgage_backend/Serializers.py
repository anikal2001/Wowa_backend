from rest_framework import serializers
from .models import Mortgage_values


class Mortgage_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage_values
        fields = ('id', 'year', 'source', 'rate', 'rate_type')
