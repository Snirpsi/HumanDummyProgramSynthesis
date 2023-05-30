#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and opens a port. """    
    
    ports = range(8000,9000)
    
    server = HTTPServer(ports, SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
