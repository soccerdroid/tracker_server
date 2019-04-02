from django.contrib.gis.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class LastLocation(models.Model):
    location = models.PointField()
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Step(models.Model):
    location = models.PointField() #default srid is 4326
    speed = models.DecimalField(default=0.000, max_digits=10, decimal_places=3)
    timestamp = models.DateTimeField(default=datetime.now)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)

    def __str__(self):
    	return self.location
    
    class Meta:
    	ordering = ["timestamp"]
    	verbose_name = "Points of routes"

class Route(models.Model):
    timestamp = models.DateTimeField(default=datetime.now)
    distance = models.DecimalField(default=0.000, max_digits=20, decimal_places=3)
    init_coord = models.PointField()
    end_coord = models.PointField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
    	return 'Route '+self.timestamp + 'of user '+self.user.username
    
    class Meta:
    	ordering = ["timestamp"]
    	verbose_name = "Routes"

class User(AbstractUser):
	pass
	
	#username
	#psw
	#salt

'''class Transport(models.Model):
	model
	type
'''