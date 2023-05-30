#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and iterates over all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        
        