#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers and opens all ports. """    
    
    ports = openports()
    
    for port in ports:
        
        port