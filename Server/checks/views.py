from django.shortcuts import render
from rest_framework import viewsets
from .models import Printer, Check
from .serializers import  PrinterSerializer, CheckSerializer

class PrinterViewSet(viewsets.ModelViewSet):
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()

class CheckViewSet(viewsets.ModelViewSet):
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
