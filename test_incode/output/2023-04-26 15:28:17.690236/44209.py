#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or removes a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start the server
    server.serve_forever()
    
