from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instances into JSON formats"""

    class Meta:
        """ Meta class to map serializer's fields with the model fields"""
        model = Employee
        fields = ('id', 'full_name', 'phone_number', 'company', 'department', 'occupation')
        read_only_fields = ('full_name', 'phone_number', 'company', 'department', 'occupation')


