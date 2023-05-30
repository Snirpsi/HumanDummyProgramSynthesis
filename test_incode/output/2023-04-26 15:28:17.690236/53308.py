#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and prints all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print(port)
        
