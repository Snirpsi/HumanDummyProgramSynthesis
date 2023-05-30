#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or returns all ports. """    
    
    ports = []
    
    while True:
        ports.append(input("Enter port number: "))
        
        if len(ports) == 2:
            break
    
    ports = ports.