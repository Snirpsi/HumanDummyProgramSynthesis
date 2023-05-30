#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and enumerates a port. """    
    ports = enumeratePorts()
    
    for port in ports:
        print(port)
        
