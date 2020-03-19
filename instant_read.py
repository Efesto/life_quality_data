import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	reading = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	printf("{reading[0].strftime('%Y-%m-%d %H:%M:%S')}, {reading[1]}C {reading[2]}\\%")
except KeyboardInterrupt:	
	pass
