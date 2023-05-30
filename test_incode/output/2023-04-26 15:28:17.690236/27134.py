#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_remove = []
    
    for port in range(0, 65535):
        