import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from repository import mysql


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17
INTERVAL = 60 * 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		repo = mysql.MySql()
	
		humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)		

		if humidity is not None and temperature is not None:
			repo.insert_reading(time, temperature, humidity)			
		else:
			print("Nope")
		time.sleep(INTERVAL)
except KeyboardInterrupt:	
	pass
