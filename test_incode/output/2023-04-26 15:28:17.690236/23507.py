#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a client
    