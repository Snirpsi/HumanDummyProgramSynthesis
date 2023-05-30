#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and iterates over all ports. """    
    
    ports = range(5000, 5999)
    
    for port in ports:
        