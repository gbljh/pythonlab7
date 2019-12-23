from rest_framework import serializers
from .models import SensorCategory
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = '__all__'
            