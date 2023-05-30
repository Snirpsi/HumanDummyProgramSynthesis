#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or calculates user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start a client
    