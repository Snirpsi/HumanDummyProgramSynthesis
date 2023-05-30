#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and opens fruits. """    
    
    # Start a web server
    server = HTTPServer(('0.0.0.0', 8080), FruitHandler)
    
    # Start a web server
    