from rest_framework import serializers
from .models import employee


class emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields =('firstname', 'lastname')
        # fields = '__all__'
