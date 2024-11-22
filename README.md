# Data Science Summit 2024 - OpenLineage Demo

This repository contains the demo setup for the Data Science Summit 2024 presentation on OpenLineage.

## Setup

To set up the demo environment, you will need Docker and Docker Compose installed on your machine.

### Starting the Environment

To start the environment, run the following command:

```sh
docker-compose -f docker-compose.airflow.yml -f docker-compose.marquez.yml -f docker-compose.spark.yml up
```

### Stopping the Environment

To stop the environment and remove the volumes, run the following command:

```sh
docker-compose -f docker-compose.airflow.yml -f docker-compose.marquez.yml -f docker-compose.spark.yml down -v
```

## About

This demo showcases the integration of OpenLineage with Apache Airflow, Marquez, and Apache Spark.

For more information, visit the [OpenLineage](https://openlineage.io/) website.

## License

This project is licensed under the MIT License.