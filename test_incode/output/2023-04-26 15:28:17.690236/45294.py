#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Ports</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<h1>Ports</h1>')
            self.wfile.write(b'<table>')
            self.wfile.write(b'<tr><th>Port</th><th>Status</th></tr>')
            
            for port in range(1, 65535):
                self.wfile.write(b'<tr><td>' + str(port) + '</td><td>' + 
                    str(port) + ' is ' + 
                    str(port-