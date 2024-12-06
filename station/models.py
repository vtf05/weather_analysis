from django.db import models

class WeatherStation(models.Model):
    """
    Represents a weather station.
    """
    name = models.CharField(max_length=100, unique=True)  # Name of the weather station, must be unique
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional field for station location
    state = models.CharField(max_length=50, blank=True, null=True)  # State of the station
    
    def __str__(self):
        return self.name  # String representation of the WeatherStation object


class WeatherRecord(models.Model):
    """
    Represents a weather data record.
    """
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, related_name="weather_records")  # Foreign key to WeatherStation
    date = models.DateField()  # Date of the weather record
    max_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)  # Max temperature in °C
    min_temp = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)  # Min temperature in °C
    precipitation = models.DecimalField(max_digits=7, decimal_places=1, null=True, blank=True)  # Precipitation in mm

    class Meta:
        unique_together = ("station", "date")  # Ensure no duplicate records for the same station and date
        ordering = ["date"]  # Default ordering by date
    
    def __str__(self):
        return f"WeatherRecord({self.station.name}, {self.date})"  # String representation of the WeatherRecord object


class AnnualWeatherStats(models.Model):
    """
    Represents annual weather statistics for a station.
    """
    station = models.ForeignKey('WeatherStation', on_delete=models.CASCADE, related_name='annual_stats')  # Foreign key to WeatherStation
    year = models.IntegerField()  # Year of the statistics
    avg_max_temp = models.FloatField(null=True, blank=True)  # Average maximum temperature in degrees Celsius
    avg_min_temp = models.FloatField(null=True, blank=True)  # Average minimum temperature in degrees Celsius
    total_precipitation = models.FloatField(null=True, blank=True)  # Total precipitation in centimeters

    class Meta:
        unique_together = ('station', 'year')  # Ensure no duplicate records for the same station and year
        ordering = ['station', 'year']  # Default ordering by station and year