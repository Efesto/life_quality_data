from influxdb import InfluxDBClient
import os
import time

from dotenv import load_dotenv
load_dotenv()

class InfluxDB:
  def insert_temperature_and_humidity(self, temperature, humidity):
    data = [
        {
          "measurement": "DHT-22",
            "time": self.time(),
            "fields": {
              "temperature" : temperature,
              "humidity": humidity
            }
        }
      ]

    # Send the JSON data to InfluxDB
    self.client().write_points(data)

  def insert_co2_and_tvoc(self, CO2, TVOC):
    data = [
            {
              "measurement": "CCS811",
                "time": self.time(),
                "fields": {
                  "co2" : CO2,
                  "TVOC": TVOC
                }
            }
          ]

    # Send the JSON data to InfluxDB
    self.client().write_points(data)

  def time(self):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
  
  def client(self):
    host="localhost"
    port=8086
    user=os.environ['INFLUXDB_COLLECTOR_USER_NAME']
    password=os.environ['INFLUXDB_COLLECTOR_USER_PASSWORD']
    dbname="readings"

    return InfluxDBClient(host, port, user, password, dbname)