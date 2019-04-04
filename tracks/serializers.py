from .models import *
from rest_framework import serializers


class LastLocationSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField(many=False,read_only=True,slug_field='username')
	location = serializers.SerializerMethodField()

	class Meta:
		model = LastLocation
		fields = ('location', 'timestamp', 'user')

	def get_location(self, obj):
		if obj.location:
			return {
				"lat": obj.location.x,
				"lng" : obj.location.y
			}


class StepSerializer(serializers.ModelSerializer):
	location = serializers.SerializerMethodField()

	class Meta:
		model = Step
		fields = ('location', 'timestamp', 'route')

	def get_location(self, obj):
		if obj.location:
			return {
				"lat": obj.location.x,
				"lng" : obj.location.y
			}

class RouteSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField(many=False,read_only=True,slug_field='username')
	steps = StepSerializer(many=True,  read_only=True)

	class Meta:
		model = Route
		fields = ('distance', 'timestamp', 'user', 'steps')
