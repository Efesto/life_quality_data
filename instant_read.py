import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	print("{}C {}%".format(temperature, humidity))
except KeyboardInterrupt:
	pass
