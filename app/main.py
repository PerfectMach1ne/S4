#!/bin/python3.12

import os, socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler


print("Serving NW4 screenshots at 192.168.1.229:8044")

class CORSMiddleware(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    
    def do_OPTIONS(self):
        # For CORS preflight requests
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=CORSMiddleware):
    server_address=('192.168.1.229', 8044)
    httpd = server_class(server_address, handler_class)
    # httpd = socketserver.TCPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    os.chdir('/store/nw4ss/')
    run()
