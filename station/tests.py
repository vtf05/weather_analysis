from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import WeatherRecord, WeatherStation, AnnualWeatherStats

class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.station = WeatherStation.objects.create(name="TestStation", location="TestLocation")
        self.record = WeatherRecord.objects.create(
            station=self.station,
            date="2024-12-01",
            max_temp=150,
            min_temp=50,
            precipitation=100
        )
        self.stats = AnnualWeatherStats.objects.create(
            station=self.station,
            year=2024,
            avg_max_temp=15.0,
            avg_min_temp=5.0,
            total_precipitation=10.0
        )

    def test_weather_list(self):
        response = self.client.get(reverse('weather-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_weather_stats_list(self):
        response = self.client.get(reverse('weather-stats-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_weather_list_filter(self):
        response = self.client.get(reverse('weather-list') + '?station=' + str(self.station.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_weather_stats_list_filter(self):
        response = self.client.get(reverse('weather-stats-list') + '?year=2024')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)