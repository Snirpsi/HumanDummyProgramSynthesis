#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Create a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
