#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or adds all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing all available ports. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = []
            for port in range(1024):
                ports.append(port)
            
            self.wfile.write(bytes(ports, 'utf-8'))
    
    server = HTTPServer(("", 0), MyHandler)
    server.serve_forever()
    
