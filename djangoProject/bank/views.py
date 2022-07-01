
from rest_framework import generics

from djangoProject.serializers import *

# C
class BankCreateAPIView(generics.CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


# R
class BankAPIView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankAllAPIView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer