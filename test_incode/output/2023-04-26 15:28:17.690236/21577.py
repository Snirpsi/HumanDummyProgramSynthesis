#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and iterates over a list of numbers. """    
    ports = range(10000, 20000)
    
    for port in ports:
        