#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or multiplyes a port. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start it
    server.serve_forever()
