#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or removes user input. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        ports.remove(port)
        
    print(ports)
    
