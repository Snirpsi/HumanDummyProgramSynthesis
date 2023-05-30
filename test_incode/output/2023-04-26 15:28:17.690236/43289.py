#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and removes fruits. """    
    
    # Instantiate our server
    server = FruitServer()
    
    # Start the server
    server.serve_forever()
    
    # Stop the server
    server.server_close()
    
