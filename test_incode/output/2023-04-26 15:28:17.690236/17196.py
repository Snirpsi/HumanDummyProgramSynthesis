#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    # Create a webserver
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
