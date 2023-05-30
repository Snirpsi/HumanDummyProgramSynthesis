#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or converts fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
