#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or iterates over user input. """    
    
    ports = input("Enter ports: ")
    
    ports = ports.split()
    
    for port in ports:
        
        port = int(port)
        
        port