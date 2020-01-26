from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from repository import mysql

SERVER_PORT = 8080

class FileHandler(BaseHTTPRequestHandler):
	def do_GET(self):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			repo = mysql.MySql()

			for reading in repo.get_all					
			self.wfile.write(f"{reading[0]}, {reading[1]} {reading[2]}<br />")

with socketserver.TCPServer(("", SERVER_PORT), FileHandler) as httpd:
    print("serving at port", SERVER_PORT)
    httpd.serve_forever()