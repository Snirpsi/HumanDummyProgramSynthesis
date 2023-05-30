#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or calculates words. """    
    
    # Create a server
    server = HTTPServer(("", 80), FruitCalculator)
    
    # Start it
    server.serve_forever()
    
