#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port. """    
    port = 1
    while port < 65535:
        port = port + 1
        print("Port {} is open".format(port))
        
