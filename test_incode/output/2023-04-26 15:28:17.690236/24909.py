#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    # Instantiate the server
    server = FruitServer()
    
    # Start the server
    server.serve_forever()
    
