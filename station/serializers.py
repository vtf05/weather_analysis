from rest_framework import serializers
from .models import WeatherRecord, AnnualWeatherStats

class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = ['station', 'date', 'max_temp', 'min_temp', 'precipitation']

class AnnualWeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualWeatherStats
        fields = ['station', 'year', 'avg_max_temp', 'avg_min_temp', 'total_precipitation']
