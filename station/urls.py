from django.urls import path
from .views import WeatherRecordListView, AnnualWeatherStatsListView

urlpatterns = [
    path('weather', WeatherRecordListView.as_view(), name='weather-list'),
    path('weather/stats', AnnualWeatherStatsListView.as_view(), name='weather-stats-list'),
]
