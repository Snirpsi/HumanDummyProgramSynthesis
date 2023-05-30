#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and removes fruits. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), Fruit)
    
    # Start it
    server.serve_forever()
    
