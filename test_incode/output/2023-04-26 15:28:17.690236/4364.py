#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and enumerates a list of numbers. """    
    
    port = '/dev/ttyUSB0'
    
    ports = enumeratePorts(port)
    
    for port in ports:
        print(port)
        
    
