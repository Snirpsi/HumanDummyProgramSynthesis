#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or adds a list of words. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), FruitServer)
    
    # Start it
    server.serve_forever()
    
