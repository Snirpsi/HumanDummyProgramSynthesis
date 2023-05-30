#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or returns fruits. """    
    
    # Create a server
    server = HTTPServer(('', 80), FruitServer)
    
    # Start it
    server.serve_forever()
    
