#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or multiplyes a list of numbers. """    
    
    # Create a simple webserver
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
