#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and multiplyes a port. """    
    
    # Create a webserver
    server = HTTPServer(('', 8080), FruitAndMultiplyPortHandler)
    
    # Start it
    server.serve_forever()

