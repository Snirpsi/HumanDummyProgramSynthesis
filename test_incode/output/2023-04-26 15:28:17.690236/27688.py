#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or stores words. """    
    
    # Create a server
    server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
