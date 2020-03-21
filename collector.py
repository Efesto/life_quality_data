import time
from repository import influxdb
from sensors import dht, ccs811

INTERVAL = 60

try:
	while True:
		repo = influxdb.InfluxDB()
	
		humidity, temperature = dht.DHT().read()		
		eCO2, TVOC = ccs811.CCS811().read()

		if humidity is not None and temperature is not None:
			repo.insert_temperature_and_humidity(temperature, humidity)

		if eCO2 is not None and TVOC is not None:
			repo.insert_co2_and_tvoc(eCO2, TVOC)

		time.sleep(INTERVAL)
except KeyboardInterrupt:	
	pass
