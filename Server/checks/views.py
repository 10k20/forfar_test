from django.shortcuts import render
from rest_framework import viewsets
from .models import Printer, Check
from .serializers import  PrinterSerializer, CheckSerializer
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
    return render(request, "index.html")

class PrinterViewSet(viewsets.ModelViewSet):
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()

class CheckViewSet(viewsets.ModelViewSet):
    serializer_class = CheckSerializer
    queryset = Check.objects.all()
 
