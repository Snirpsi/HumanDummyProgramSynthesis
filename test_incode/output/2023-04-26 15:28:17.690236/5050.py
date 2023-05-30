#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or returns numbers. """    
    
    # Create a simple server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start it
    server.serve_forever()
    
