#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and calculates fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitCalculator)
    
    # Start it
    server.serve_forever()
    
