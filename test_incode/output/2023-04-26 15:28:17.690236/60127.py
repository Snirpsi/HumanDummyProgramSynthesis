#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or enumerates a list of numbers. """    
    
    ports = range(8000, 8100)
    
    for port in ports:
        open