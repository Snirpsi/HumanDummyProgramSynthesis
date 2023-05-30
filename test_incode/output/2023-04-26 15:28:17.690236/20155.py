#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and adds all ports. """    
    
    # Create the server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
