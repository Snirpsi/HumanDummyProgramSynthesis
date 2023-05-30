#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    
    ports = range(10000, 20000, 100)
    
    while True:
        for port in ports:
            print('