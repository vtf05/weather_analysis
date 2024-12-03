Problem 1: Data Modeling

# Weather Analysis

## Database Choice: PostgreSQL for relational database

### Data Models

#### WeatherStation Model

- Represents weather stations, each uniquely identified by their name or ID.
- Includes fields for station name, location (optional), and state.

#### WeatherRecord Model

- Stores weather data linked to a weather station and a specific date.
- Fields include date, max temperature, min temperature, and precipitation, with support for nullable fields to handle missing values.
- Constraints ensure data integrity, such as uniqueness of the combination of station and date.

## Problem 2: Data Ingestion

### Command

```bash
python manage.py ingest_weather_data --data-dir=wx_data
```

### Approach

#### File Parsing

- Read raw text files from the specified directory.
- Parse records, skipping invalid lines and logging issues.

#### Duplicate Handling

- Use database constraints or checks within the ORM to ensure uniqueness for the same station and date.
- Before insertion, check for existing records using a combination of station and date.

#### Batch Insert

- Insert records in batches for performance optimization.
- Use transactions to roll back in case of errors.

#### Logging

- Log the start and end time of ingestion.
- Record the number of rows processed and skipped due to errors or duplicates.

## Problem 3: Data Analysis

### Command

```bash
python manage.py calculate_annual_stats
```

### New Data Model

#### AnnualWeatherStats Model

- Stores yearly aggregated statistics for each weather station.
- Fields include average max/min temperatures and total precipitation.
- Uses NULL for fields that cannot be calculated due to missing data.

### Steps to Calculate

#### Group By Year and Station

- Query the WeatherRecord table grouped by year and station.

#### Calculations

- Ignore missing data (-9999).
- Compute averages for max/min temperatures and sum precipitation.

#### Insert or Update Results

- Check for existing records in AnnualWeatherStats.
- Insert new or update existing records with recalculated values.

#### Optimization

- Index the WeatherRecord table by station and date for efficient querying.
- Use bulk operations for calculations and insertions.

## Problem 4: REST API

### Framework: Django REST Framework (DRF)

#### Setup

To run the application, clone the repository using:

```bash
git clone https://github.com/vtf05/weather_analysis.git
```

Initialize the virtual environment using:

```bash
pipenv shell
```

Install all the required libraries:

```bash
pipenv install
```

To delete existing data, run:

```bash
python manage.py flush
```

To run the application, use:

```bash
python manage.py runserver
```

To run the tests, use:

```bash
python manage.py test
```

#### Endpoints

The following endpoints are available in the application to fetch weather and year-specific statistics:

- `/weather`
- `/weather/stats`

#### API Documentation

Swagger/OpenAPI documentation is generated using `drf-yasg`. You can access the API documentation at:

- `/redoc`
- `/swagger`

## Deployment in AWS

### AWS Tools and Services

#### API Deployment

- We can use Amazon Elastic Kubernetes Service (EKS) or AWS Elastic Beanstalk for deploying the Django API.
- Optionally, expose the API via Amazon API Gateway.

#### Database

- We can host the database on Amazon RDS with PostgreSQL for high availability and automatic backups.
- Secure access using VPC and AWS Secrets Manager for credentials.

#### Data Ingestion

- AWS Lambda for running the ingestion logic triggered by an S3 upload or scheduled via Amazon EventBridge.
- Alternatively, use Amazon ECS Fargate for containerized ingestion tasks.

#### Storage

- Store raw weather files in Amazon S3 with event triggers for ingestion.

#### Monitoring

- we can use Amazon CloudWatch for application and ingestion logs.
- Set up CloudWatch Alarms for error notifications via Amazon SNS.

#### Deployment Pipeline

- We can use AWS CodePipeline and AWS CodeBuild for CI/CD to deploy the API and ingestion tasks.
