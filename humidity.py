import Adafruit_DHT
import RPi.GPIO as GPIO
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN=17
INTERVAL = 60 * 10

FILE_PATH="/home/pi/share/readings.csv"

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
	while True:
		file = open(FILE_PATH, "a")
		humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

		if humidity is not None and temperature is not None:
			line = "{0} {1} {2:0.1f}*C {3:0.1f}%\n".format(time.strftime('%d/%m/%y'), time.strftime('%H:%M'), temperature, humidity)
			print(line)
			file.write(line)
		else:
			print("Nope")
		file.close()
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	print("Ciao capo")
	pass
