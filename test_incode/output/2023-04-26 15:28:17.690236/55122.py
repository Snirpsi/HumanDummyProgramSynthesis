#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or iterates over a port. """    
    port = 1
    while True:
        port = port + 1
        print("Port {} is now listening.".format(port))
        
