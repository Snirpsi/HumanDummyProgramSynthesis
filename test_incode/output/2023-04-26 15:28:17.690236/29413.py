#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and iterates over all ports. """    
    
    ports = range(8000, 9000)
    
    for port in ports:
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()
    
