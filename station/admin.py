from django.contrib import admin
from station.models import WeatherStation, WeatherRecord, AnnualWeatherStats
# Register your models here.
admin.site.register(WeatherStation)
admin.site.register(WeatherRecord)
admin.site.register(AnnualWeatherStats)