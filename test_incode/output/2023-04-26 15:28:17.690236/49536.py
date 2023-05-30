#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and multiplyes all ports. """    
    port = 1
    
    while(True):
        port = port * 10
        print(port)
        
