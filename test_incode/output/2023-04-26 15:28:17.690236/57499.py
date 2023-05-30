#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and removes a list of words. """    
    
    ports = range(65536)
    
    while True:
        for port in ports:
            