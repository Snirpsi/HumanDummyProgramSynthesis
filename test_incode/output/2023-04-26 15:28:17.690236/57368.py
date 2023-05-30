#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and prints all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        