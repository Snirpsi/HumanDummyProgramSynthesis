#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and calculates all ports. """    
    
    # Create a server and listen for connections
    server = HTTPServer(('localhost', 8080), FruitHandler)
    server.serve_forever()
