<<<<<<< HEAD
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
=======
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
>>>>>>> 08da0863952d53475e8a2cc00f476ab899c49fba
        #fields = ('id','fullname','emp_code','mobile')