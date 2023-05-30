#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or returns all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = []
            
            for port in range(1, 65535):
                ports.append(port)
            
            self.wfile.write(b'<html><head><title>Ports</title></head>')
            self.wfile.write(b'<body>')
            
            for port in ports:
                self.wfile.write(b'<p>Port {}</p>'.format(port))
            
            self.wfile.write(b'</body></html>')
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving on port 8080')
    
    httpd.serve_forever()
    
