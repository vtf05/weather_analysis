from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import WeatherRecord, AnnualWeatherStats
from .serializers import WeatherRecordSerializer, AnnualWeatherStatsSerializer

# Custom pagination class to set default and maximum page sizes
class StandardResultsPagination(PageNumberPagination):
    page_size = 10  # Default number of records per page
    page_size_query_param = 'page_size'  # Allow client to set page size using this query parameter
    max_page_size = 100  # Maximum number of records per page

# List view for WeatherRecord model with filtering and pagination
class WeatherRecordListView(generics.ListAPIView):
    queryset = WeatherRecord.objects.all()  # Queryset to retrieve all WeatherRecord objects
    serializer_class = WeatherRecordSerializer  # Serializer class to convert WeatherRecord objects to JSON
    filter_backends = [DjangoFilterBackend]  # Enable filtering using DjangoFilterBackend
    filterset_fields = ['date', 'station']  # Allow filtering by 'date' and 'station' fields
    pagination_class = StandardResultsPagination  # Use custom pagination class

# List view for AnnualWeatherStats model with filtering and pagination
class AnnualWeatherStatsListView(generics.ListAPIView):
    queryset = AnnualWeatherStats.objects.all()  # Queryset to retrieve all AnnualWeatherStats objects
    serializer_class = AnnualWeatherStatsSerializer  # Serializer class to convert AnnualWeatherStats objects to JSON
    filter_backends = [DjangoFilterBackend]  # Enable filtering using DjangoFilterBackend
    filterset_fields = ['year', 'station']  # Allow filtering by 'year' and 'station' fields
    pagination_class = StandardResultsPagination  # Use custom pagination class