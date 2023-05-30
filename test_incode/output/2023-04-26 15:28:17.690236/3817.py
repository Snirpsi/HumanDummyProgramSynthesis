#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or adds a list of numbers. """    
    ports = range(8000, 9000)
    
    # Add a list of ports to the server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.add_