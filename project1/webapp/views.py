from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView, status, Response
from .models import employee
from .serializers import emp_serializer


# Create your views here.


class emp_list(APIView):
    def get(self, request):
        emp1 = employee.objects.all()

        serializer = emp_serializer(emp1, many=True)
        return Response(serializer.data)
