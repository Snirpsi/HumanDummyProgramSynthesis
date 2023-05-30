#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and iterates over words. """    
    
    # Create a simple web server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
