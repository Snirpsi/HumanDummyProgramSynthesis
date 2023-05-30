#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and prints a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()
    
