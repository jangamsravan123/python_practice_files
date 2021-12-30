from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.29.138"

PORT = 8000


class httpServerHandle(BaseHTTPRequestHandler) :
	def do_GET(self) :
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(bytes("<html><body><h1>Hello World</h1></body></html>", "utf-8"))


	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()
		self.wfile.write(bytes('{"name" : "sravan"}', "utf-8"))

server = HTTPServer((HOST, PORT), httpServerHandle)
print("server is running......")
server.serve_forever()

server.server_close()

print("server closed")
