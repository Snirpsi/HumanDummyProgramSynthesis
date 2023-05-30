#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and converts a list of numbers. """    
    
    # Create a webserver
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
