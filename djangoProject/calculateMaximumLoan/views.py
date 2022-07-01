import json

import requests
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoProject.models import *
from djangoProject.serializers import *
from django.core import serializers

from .tasks import *

verify = "http://localhost:8000/verify/"
bankEP = "http://localhost:8000/bank/"

# C
class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# R
class TaskAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAllAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# D
class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializer


class TaskPostAPIView(APIView):
    def post(self, request):
        customerSerializer = CustomerSerializer(data=request.data.get("customer"))
        customer = customerSerializer.initial_data
        bank_id = request.data.get("bank_id")

        verify_response = requests.post(verify, request.data.get("customer"))
        if not verify_response:
            print("customer info not verified")
            return Response("Invalid customer info", status=status.HTTP_406_NOT_ACCEPTABLE)

        bank_response = requests.get(bankEP + bank_id.__str__() + "/")


        if customer["creditScore"] >= bank_response.json().get("minimumCreditScore"):
            return Response({"result" : customer["creditScore"]*1000, "reason" : ""})
        return Response({"result" : 0, "reason" : "Bank Criteria not met"})
