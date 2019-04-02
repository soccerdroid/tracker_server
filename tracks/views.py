from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import *


def home(request):
	if request.method == 'GET':
		return render(request,"index.html");