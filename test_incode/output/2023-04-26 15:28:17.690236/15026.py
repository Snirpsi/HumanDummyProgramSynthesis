#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    # Create a simple webserver
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    webserver.serve_forever()
    
