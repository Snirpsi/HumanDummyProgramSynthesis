#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or opens all ports. """    
    
    ports = openports()
    
    for port in ports:
        
        if port in 