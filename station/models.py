
from django.db import models

class WeatherStation(models.Model):
    """
    Represents a weather station.
    """
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional field for station location
    state = models.CharField(max_length=50, blank=True, null=True)  # State of the station
    
    def __str__(self):
        return self.name


class WeatherRecord(models.Model):
    """
    Represents a weather data record.
    """
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, related_name="weather_records")
    date = models.DateField()
    max_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)  # Max temp in °C
    min_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)  # Min temp in °C
    precipitation = models.DecimalField(max_digits=7, decimal_places=1, null=True, blank=True)  # Precipitation in mm

    class Meta:
        unique_together = ("station", "date")  # Ensure no duplicate records for the same station and date
        ordering = ["date"]  # Default ordering by date
    
    def __str__(self):
        return f"WeatherRecord({self.station.name}, {self.date})"


from django.db import models

class AnnualWeatherStats(models.Model):
    station = models.ForeignKey('WeatherStation', on_delete=models.CASCADE, related_name='annual_stats')
    year = models.IntegerField()
    avg_max_temp = models.FloatField(null=True, blank=True)  # Average maximum temperature in degrees Celsius
    avg_min_temp = models.FloatField(null=True, blank=True)  # Average minimum temperature in degrees Celsius
    total_precipitation = models.FloatField(null=True, blank=True)  # Total precipitation in centimeters

    class Meta:
        unique_together = ('station', 'year')
        ordering = ['station', 'year']
