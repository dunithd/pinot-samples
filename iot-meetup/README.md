# Artifacts for the meetup - Analyzing IoT data with Apache Kafka and Apache Pinot

This repository contains the samples used during the meetup.

## Use case

![](/diagrams/demo.png "Solution architecture")

## Prerequisites

Clone the repository and navigate to the `iot-meetup` folder.

```bash
git clone git@github.com:dunithd/pinot-samples.git
cd iot-meetup
```

## Start the Kafka+Pinot cluster

Run the following command from the root level to start up an Apache Pinot cluster, along with a single instance of Apache Kafka and Zookeeper.

```bash
docker-compose up -d
```

Create a Kafka topic called `readings` using:

```bash
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
--create --bootstrap-server kafka:9092 --topic readings
```

## Create the schemas and tables in Pinot

Run the following command to create the schema and table for the `readings` real-time table.

```bash
docker exec -it pinot-controller /opt/pinot/bin/pinot-admin.sh AddTable \
-tableConfigFile /config/readings_table.json \
-schemaFile /config/readings_schema.json -exec
```

Create the `sensors` offline table using:

```bash
docker exec -it pinot-controller /opt/pinot/bin/pinot-admin.sh AddTable \
-tableConfigFile /config/sensors_table.json \
-schemaFile /config/sensors_schema.json -exec
```

Ingest sample records to `sensors` table with:

```bash
docker exec -it pinot-controller /opt/pinot/bin/pinot-admin.sh LaunchDataIngestionJob \
-jobSpecFile /config/sensors_job_spec.yml
```

## Install and configure Redash locally

Follow [this](https://redash.io/help/open-source/dev-guide/docker) guide to install and configure Redash on your local machine with Docker.

Configure [Python data source](https://redash.io/help/data-sources/querying/python#Writing-Queries) inside Redash.

## Start producers

This sample contains four data producers to simulate four trucks. They are located in the `/producers` folder.

- 100_producer.py - Simulates a regular truck with sensor_id 100
- 101_producer.py - Simulates a speeding truck with sensor_id 101
- 102_producer.py - Simulates an idling truck with sensor_id 102
- 103_producer.py - Simulates a truck with sensor_id 103, travelling from SFO to Golden Gate bridge

Start them one by one and see the `readings` topic getting populated with sensor readings coming from all the trucks.

## Run Pinot queries

You can find the Pinot queries demonstrated during the meetup inside the `/pinot-quries` folder.

## Run Redash queries

You can find the Redash queries written using Python inside `/redash` folder. Create them inside Redash and run to see results.

## Install Jupyter notebooks 

Run Jupyter notebooks in a Docker container using:

```bash
docker run -p 8888:8888 jupyter/scipy-notebook
```

Run the code inside `jupyter-notebooks` folder in a new notebook. Make sure to install required Python libraries including Pandas and Matplotlib.

Enjoy the project!

