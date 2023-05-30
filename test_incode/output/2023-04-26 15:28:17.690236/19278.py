#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits and prints words. """    
    
    # Create a webserver
    server = HTTPServer(('', 80), FruitCalculator)
    
    # Start it
    server.serve_forever()
