#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or removes a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    ports = port.split()
    
    ports.remove('USB')
    
    for port in ports:
        print(port)
        
