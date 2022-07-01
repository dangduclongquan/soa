
from djangoProject.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from rest_framework import generics


class VerifyAPIView(APIView):
    def post(self, request):
        print("verifying customer info")
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.create()
        else:
            if not Customer.objects.all().filter(creditScore=serializer.initial_data["creditScore"]).exists():
                print("cannot find customer with credit Score")
                return Response(False, status=status.HTTP_400_BAD_REQUEST)
            customer = Customer.objects.all().filter(creditScore=serializer.initial_data["creditScore"])[0]
            if customer.name != serializer.initial_data["name"]:
                print("name does not match")
                return Response(False, status=status.HTTP_400_BAD_REQUEST)
            if customer.creditScore.__str__() != serializer.initial_data["creditScore"].__str__():
                print("credit score does not match")
                return Response(False, status=status.HTTP_400_BAD_REQUEST)
        today = datetime.datetime.now().date()
        print(customer.dob > today)
        if customer.dob > today:
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(True)

