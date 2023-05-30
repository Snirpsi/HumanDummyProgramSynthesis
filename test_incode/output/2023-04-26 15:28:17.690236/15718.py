#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and opens a port. """    
    
    ports = range(8000, 8008)
    
    for port in ports:
        server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
        server.serve_forever()
