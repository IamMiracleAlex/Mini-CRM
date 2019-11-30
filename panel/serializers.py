# from rest_framework import serializers


# class EmployeeSerializer(serializers.Serializer):
#     first_name  = serializers.CharField(max_length=60)
#     last_name   = serializers.CharField(max_length=60)
#     email       = serializers.EmailField(max_length=60) 
#     phone       = serializers.CharField(max_length=11)


from rest_framework import serializers
from .models import Employee
      
class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ('first_name', 'last_name','email','company','phone')    