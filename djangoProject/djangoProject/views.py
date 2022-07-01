
from rest_framework import generics

from .serializers import *


# C
class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# R
class CustomerInformationAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAllAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# U
class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


# Transaction History
class TransactionHistoryAPIView(generics.ListAPIView):
    serializer_class = LoanSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        cid = self.kwargs.get(self.lookup_url_kwarg)
        loans = Loan.objects.filter(customer=cid)
        return loans


# Loan C
class LoanCreateAPIView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


# Loan R
class LoanAPIView(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanAllAPIView(generics.ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


# Loan U
class LoanUpdateAPIView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()





