import os
import logging
from datetime import datetime
from django.core.management.base import BaseCommand
from station.models import WeatherStation, WeatherRecord

class Command(BaseCommand):
    help = "Ingest weather data from raw text files into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            '--data-dir',
            type=str,
            required=True,
            help="Path to the directory containing the weather data files.",
        )

    def handle(self, *args, **options):
        data_dir = options['data_dir']

        # Logging setup
        logger = logging.getLogger('weather_ingest')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('weather_ingest.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

        start_time = datetime.now()
        logger.info("Weather data ingestion started.")
        self.stdout.write("Weather data ingestion started.")

        record_count = 0
        try:
            # Iterate over all files in the data directory
            for filename in os.listdir(data_dir):
                file_path = os.path.join(data_dir, filename)
                if os.path.isfile(file_path):
                    station_name = os.path.splitext(filename)[0]  # Use filename as station name
                    station, _ = WeatherStation.objects.get_or_create(name=station_name)

                    with open(file_path, 'r') as f:
                        for line in f:
                            date_str, max_temp, min_temp, precipitation = line.strip().split('\t')
                            date = datetime.strptime(date_str, '%Y%m%d').date()

                            # Convert -9999 to None
                            max_temp = None if max_temp == '-9999' else int(max_temp) / 10.0
                            min_temp = None if min_temp == '-9999' else int(min_temp) / 10.0
                            precipitation = None if precipitation == '-9999' else int(precipitation) / 10.0

                            # Check for duplicates
                            if not WeatherRecord.objects.filter(station=station, date=date).exists():
                                WeatherRecord.objects.create(
                                    station=station,
                                    date=date,
                                    max_temp=max_temp,
                                    min_temp=min_temp,
                                    precipitation=precipitation
                                )
                                record_count += 1

            logger.info(f"Weather data ingestion completed. {record_count} records ingested.")
            self.stdout.write(f"Weather data ingestion completed. {record_count} records ingested.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            self.stderr.write(f"An error occurred: {str(e)}")

        end_time = datetime.now()
        logger.info(f"Ingestion completed. Start: {start_time}, End: {end_time}")
        self.stdout.write(f"Ingestion completed. Start: {start_time}, End: {end_time}")
