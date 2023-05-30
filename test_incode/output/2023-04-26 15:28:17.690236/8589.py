#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), FruitCalculator)
    
    # Start it
    server.serve_forever()
    
