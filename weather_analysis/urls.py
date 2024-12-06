from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Configure the schema view for API documentation using drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",  # Title of the API documentation
        default_version='v1',  # Default version of the API
        description="API documentation for weather data",  # Description of the API
        terms_of_service="https://www.google.com/policies/terms/",  # Terms of service URL
        contact=openapi.Contact(email="admin@example.com"),  # Contact information
        license=openapi.License(name="BSD License"),  # License information
    ),
    public=True,  # Make the schema view public
    permission_classes=(AllowAny,),  # Allow any user to access the schema view
)

# Define URL patterns for the application
urlpatterns = [
    path('api/', include('station.urls')),  # Include URLs from the 'station' app
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI for API documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI for API documentation
]