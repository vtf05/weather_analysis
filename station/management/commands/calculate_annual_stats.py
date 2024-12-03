import logging
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db.models import Avg, Sum, F, DecimalField
from django.db.models.functions import Cast
from station.models import WeatherRecord, AnnualWeatherStats

class Command(BaseCommand):
    help = "Calculate and store annual weather statistics for each weather station."

    def handle(self, *args, **kwargs):
        logger = logging.getLogger('weather_stats')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('weather_stats.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

        start_time = datetime.now()
        logger.info("Annual statistics calculation started.")
        self.stdout.write("Annual statistics calculation started.")

        try:
            # Annotate records to calculate annual statistics
            annual_stats = WeatherRecord.objects.values('station_id', 'date__year').annotate(
                avg_max_temp=Avg('max_temp'),
                avg_min_temp=Avg('min_temp'),
                total_precipitation=Sum(Cast(F('precipitation'), DecimalField()) / 10)  # Convert mm to cm
            )

            # Save or update the statistics in the database
            for stat in annual_stats:
                AnnualWeatherStats.objects.update_or_create(
                    station_id=stat['station_id'],
                    year=stat['date__year'],
                    defaults={
                        'avg_max_temp': stat['avg_max_temp'],
                        'avg_min_temp': stat['avg_min_temp'],
                        'total_precipitation': stat['total_precipitation']
                    }
                )

            logger.info("Annual statistics calculation completed successfully.")
            self.stdout.write("Annual statistics calculation completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            self.stderr.write(f"An error occurred: {str(e)}")

        end_time = datetime.now()
        logger.info(f"Calculation completed. Start: {start_time}, End: {end_time}")
        self.stdout.write(f"Calculation completed. Start: {start_time}, End: {end_time}")