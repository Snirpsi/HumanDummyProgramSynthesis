#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    ports = range(8000, 8100)
    
    for port in ports:
        