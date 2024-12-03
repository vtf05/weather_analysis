from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import WeatherRecord, AnnualWeatherStats
from .serializers import WeatherRecordSerializer, AnnualWeatherStatsSerializer

class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# List views for WeatherRecord with filtering , pagination.
class WeatherRecordListView(generics.ListAPIView):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'station']
    pagination_class = StandardResultsPagination

# List views for AnnualWeatherStats with filtering , pagination.
class AnnualWeatherStatsListView(generics.ListAPIView):
    queryset = AnnualWeatherStats.objects.all()
    serializer_class = AnnualWeatherStatsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'station']
    pagination_class = StandardResultsPagination
