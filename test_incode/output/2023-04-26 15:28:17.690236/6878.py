#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits and adds all ports. """    
    
    # Create a server
    server = HTTPServer(('', 80), FruitCalculator)
    
    # Start it
    server.serve_forever()
    
