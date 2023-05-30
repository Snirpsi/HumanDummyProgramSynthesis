#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    #It serves static files with an index.html file that displays the fruit list.
    #The server can be started with python3 server.py
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open('index.html').read())
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    print('serving at port', 8080)
    httpd.serve_forever()

