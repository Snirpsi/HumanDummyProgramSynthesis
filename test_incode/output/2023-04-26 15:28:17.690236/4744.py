#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
