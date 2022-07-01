from rest_framework import generics
from djangoProject.serializers import *
from djangoProject.models import *


# Create your views here.
# C
class ResultCreateAPIView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


# R
class ResultAPIView(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultAllAPIView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
