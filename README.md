# London Commute Analysis

## Introduction

Looking at how transport plays the role of a backbone of a city, this project focuses on the London Commute Experience to enable the administration to take key decisions towards the improvement of transportation services, expansion of networks and providing safer roads.

## 5 minute demo: https://www.youtube.com/watch?v=_Sutw9RaUlE

## Tools/Technologies used:

* ETL operations on static and live data feed: Apache Spark  
* Manage Live Streaming Dataset: Apache Kafka  
* Backend Database: PostgreSQL  
* Visualization: Plotly, Folium, Mapbox  
* Twitter sentiment analysis: tweepy, twython, wordcloud  
* Frontend: Dash by Plotly  

## Data Sources
The data sources are CSV files, JSON API's, live bus arrivals combining 10 GB in size obtained from Transport For London Network. In addition to this, twitter API is used to fetch live twitter data. 

## ETL Execution Instructions
* `python3 dataload_Accident.py` to execute ETL job for accident data.  
* `python3 countsdata.py` to execute ETL job for tube usage data.  
* `python3 kafkaproducer.py` to load data from HTTP and create producer  
* `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4 read.py bus` to execute Consumer for Kafka stream  
* `python3 bus_etl_data.py` to execute ETL job for bus data  
* `python3 cycledataetl.py` to execute ETL job for cycling data  
* `python3 Carpark.py` to execute ETL job for parking infrastructure data  
* `python3 accidentmaps.py` to generate Folium Maps  

## Once, the data load has finished, dashboard can be launched using the below command
* Execute python3 index.py to launch the dashboard

Note: PostgreSQL database is used and the connector postgresql-42.2.8.jar would be required.
