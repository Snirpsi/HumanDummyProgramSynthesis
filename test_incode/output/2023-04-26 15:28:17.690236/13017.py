#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or opens user input. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port < 65536:
            
            