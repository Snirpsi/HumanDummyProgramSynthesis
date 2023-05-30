#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitCalculator)
    
    # Start it
    server.serve_forever()
    
