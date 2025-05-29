from django.db import models

class WeatherStation(models.Model):
    """
    Represents a weather station.
    """
    name = models.CharField(max_length=100, unique=True)  # Name of the weather station, must be unique
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional field for station location (e.g., city or address)
    state = models.CharField(max_length=50, blank=True, null=True)  # State or region where the station is located
    
    def __str__(self):
        return self.name  # String representation of the WeatherStation object, typically used in admin or debugging


class WeatherRecord(models.Model):
    """
    Represents a weather data record.
    """
    station = models.ForeignKey(
        WeatherStation, 
        on_delete=models.CASCADE, 
        related_name="weather_records"
    )  # Foreign key linking the record to a specific weather station; deleting a station deletes its records
    date = models.DateField()  # Date of the weather record (e.g., "2023-10-01")
    max_temp = models.DecimalField(
        max_digits=5, 
        decimal_places=1, 
        null=True, 
        blank=True
    )  # Maximum temperature recorded on the date (in °C); optional field
    min_temp = models.DecimalField(
        max_digits=5, 
        decimal_places=1, 
        null=True, 
        blank=True
    )  # Minimum temperature recorded on the date (in °C); optional field
    precipitation = models.DecimalField(
        max_digits=7, 
        decimal_places=1, 
        null=True, 
        blank=True
    )  # Total precipitation recorded on the date (in mm); optional field

    class Meta:
        unique_together = ("station", "date")  # Ensures no duplicate weather records for the same station and date
        ordering = ["date"]  # Default ordering of records by date (ascending)
    
    def __str__(self):
        return f"WeatherRecord({self.station.name}, {self.date})"  # String representation for debugging or display purposes


class AnnualWeatherStats(models.Model):
    """
    Represents annual weather statistics for a station.
    """
    station = models.ForeignKey(
        'WeatherStation', 
        on_delete=models.CASCADE, 
        related_name='annual_stats'
    )  # Foreign key linking the statistics to a specific weather station; deleting a station deletes its stats
    year = models.IntegerField()  # Year for which the statistics are calculated (e.g., 2023)
    avg_max_temp = models.FloatField(
        null=True, 
        blank=True
    )  # Average of maximum temperatures recorded throughout the year (in °C); optional field
    avg_min_temp = models.FloatField(
        null=True, 
        blank=True
    )  # Average of minimum temperatures recorded throughout the year (in °C); optional field
    total_precipitation = models.FloatField(
        null=True, 
        blank=True
    )  # Total precipitation recorded throughout the year (in cm); optional field

    class Meta:
        unique_together = ('station', 'year')  # Ensures no duplicate statistics for the same station and year
        ordering = ['station', 'year']  # Default ordering of statistics by station and year (ascending)