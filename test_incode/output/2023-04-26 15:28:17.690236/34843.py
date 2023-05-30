#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or converts words. """    
    
    # Open a port on which to listen
    port = 8000
    
    # Create a server
    server = HTTPServer(('', port), FruitHandler)
    
    # Start it
    server.serve_forever()
    
