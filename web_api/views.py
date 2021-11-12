# from django.shortcuts import render

from rest_framework import viewsets
# from rest_framework.response import Response
from .models import employees
from .serializers import employeesSerializer


# class employeeList(APIView):

#     def get(self, request):
#         employees1 = employees.objects.all()
#         serializer = employeesSerializer(employees1, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass    

class employeeViewSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer