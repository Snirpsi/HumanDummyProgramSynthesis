#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and returns words. """    
    
    # Create a server
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start it
    server.serve_forever()
    
