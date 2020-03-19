from influxdb import InfluxDBClient
import os
import time

from dotenv import load_dotenv
load_dotenv()

class InfluxDB:
  def insert_temperature_and_humidity(self, temperature, humidity):
    host="localhost",
    port = 8086
    user=os.environ['INFLUXDB_COLLECTOR_USER_NAME'],
    password=os.environ['INFLUXDB_COLLECTOR_USER_PASSWORD'],
    dbname="readings"

    client = InfluxDBClient(host, port, user, password, dbname)

    data = [
        {
          "measurement": "DHT-22",
            "time": time.ctime(),
            "fields": {
              "temperature" : temperature,
              "humidity": humidity
            }
        }
      ]

    # Send the JSON data to InfluxDB
    client.write_points(data)