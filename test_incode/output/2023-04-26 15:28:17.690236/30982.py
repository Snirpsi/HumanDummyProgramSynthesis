#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    # Create a server object
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start it
    server.serve_forever()
    
