import Adafruit_DHT
import RPi.GPIO as GPIO
import time

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17
INTERVAL = 60 * 10

SERVER_PORT = 8080

FILE_PATH="/home/pi/share/readings.csv"

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class FileHandler(BaseHTTPRequestHandler):
	def do_GET(self):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			with open(FILE_PATH, 'rb') as file:
				content = file.read().decode("utf-8").replace("\n", "<br />")
				self.wfile.write(content.encode())

with socketserver.TCPServer(("", SERVER_PORT), FileHandler) as httpd:
    print("serving at port", SERVER_PORT)
    httpd.serve_forever()

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
