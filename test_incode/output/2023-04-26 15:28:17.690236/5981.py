#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and opens all ports. """    
    
    ports = openports()
    
    for port in ports:
        print(port)
        
