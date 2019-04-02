from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import *
from rest_framework import viewsets
from .serializers import LastLocationSerializer


class LastLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LastLocation.objects.all().order_by('timestamp')
    serializer_class = LastLocationSerializer


def home(request):
	if request.method == 'GET':
		return render(request,"index.html");