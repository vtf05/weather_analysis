from rest_framework import serializers
from .models import WeatherRecord, AnnualWeatherStats

class WeatherRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for WeatherRecord model.
    Converts WeatherRecord instances to JSON and vice versa.
    """
    class Meta:
        model = WeatherRecord  # Specify the model to be serialized
        fields = ['station', 'date', 'max_temp', 'min_temp', 'precipitation']  # Fields to be included in the serialization

class AnnualWeatherStatsSerializer(serializers.ModelSerializer):
    """
    Serializer for AnnualWeatherStats model.
    Converts AnnualWeatherStats instances to JSON and vice versa.
    """
    class Meta:
        model = AnnualWeatherStats  # Specify the model to be serialized
        fields = ['station', 'year', 'avg_max_temp', 'avg_min_temp', 'total_precipitation']  # Fields to be included in the serialization