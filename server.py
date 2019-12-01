

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

FILE_PATH="/home/pi/share/readings.csv"

SERVER_PORT = 8080

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