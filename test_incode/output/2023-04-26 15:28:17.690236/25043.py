#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or enumerates a port. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        
        if port[1] == 