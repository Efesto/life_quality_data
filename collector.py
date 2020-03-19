import time
from repository import influxdb
from sensors import dht

INTERVAL = 60

try:
	while True:
		repo = influxdb.InfluxDB()
	
		humidity, temperature = dht.DHT().read()

		if humidity is not None and temperature is not None:
			repo.insert_temperature_and_humidity(temperature, humidity)			
		else:
			print("Nope")
		time.sleep(INTERVAL)
except KeyboardInterrupt:	
	pass
