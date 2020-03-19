import time
from repository import mysql
from sensors import dht

try:
	while True:
		repo = mysql.MySql()
	
		humidity, temperature = dht.DHT().read()

		if humidity is not None and temperature is not None:
			repo.insert_reading(time, temperature, humidity)			
		else:
			print("Nope")
		time.sleep(INTERVAL)
except KeyboardInterrupt:	
	pass
