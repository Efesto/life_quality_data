import Adafruit_DHT
import RPi.GPIO as GPIO
import time


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17
INTERVAL = 60 * 10

FILE_PATH="/home/pi/share/readings.csv"

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		with open(FILE_PATH, 'a') as file: 
			humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

			if humidity is not None and temperature is not None:
				now_time = time.strftime('%d/%m/%y')
				today = time.strftime('%H:%M')

				line = "{0} {1} {2:0.1f}*C {3:0.1f}%\n".format(now_time, today, temperature, humidity)

				print(line)
				file.write(line)
			else:
				print("Nope")
		time.sleep(INTERVAL)
except KeyboardInterrupt:	
	pass
