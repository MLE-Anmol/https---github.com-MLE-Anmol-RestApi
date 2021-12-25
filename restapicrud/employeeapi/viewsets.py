<<<<<<< HEAD
from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

=======
from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

>>>>>>> 08da0863952d53475e8a2cc00f476ab899c49fba
#list(), retrieve(), create(), update(), destroy()