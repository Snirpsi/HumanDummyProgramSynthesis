#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or iterates over a list of words. """    
    
    # Instantiate the server
    server = FruitsServer()
    
    # Run the server
    server.serve_forever()
    
