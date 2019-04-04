from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import *
from rest_framework import viewsets
from .serializers import LastLocationSerializer, RouteSerializer, StepSerializer


class StepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Step.objects.all().order_by('timestamp')
    serializer_class = StepSerializer

class LastLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LastLocation.objects.all().order_by('timestamp')
    serializer_class = LastLocationSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Route.objects.all().order_by('timestamp')
    serializer_class = RouteSerializer


def home(request):
	if request.method == 'GET':
		return render(request,"index.html");

def rutas(request):
	if request.method == 'GET':
		return render(request,"rutas.html");