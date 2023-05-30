#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or iterates over all ports. """    
    
    ports = sys.argv[1]
    
    if ports == 'all':
        ports = range(1,65535)
    
    for port in ports:
        print(port)
    
